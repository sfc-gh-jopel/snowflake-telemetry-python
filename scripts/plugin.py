#!/usr/bin/env python3

import re
import os
import sys
from dataclasses import dataclass, field
from typing import List, Optional
from enum import IntEnum

from google.protobuf.compiler import plugin_pb2 as plugin
from google.protobuf.descriptor_pb2 import (
    FileDescriptorProto,
    FieldDescriptorProto,
    EnumDescriptorProto,
    EnumValueDescriptorProto,
    MethodDescriptorProto,
    ServiceDescriptorProto,
    DescriptorProto,
)
from jinja2 import Environment, FileSystemLoader
import black
import isort.api

class WireType(IntEnum):
    VARINT = 0
    I64 = 1
    LEN = 2
    I32 = 5

@dataclass
class ProtoTypeDescriptor:
    name: str
    wire_type: WireType
    python_type: str
    default_val: str

proto_type_to_descriptor = {
    FieldDescriptorProto.TYPE_BOOL: ProtoTypeDescriptor("bool", WireType.VARINT, "bool", "False"),
    FieldDescriptorProto.TYPE_ENUM: ProtoTypeDescriptor("enum", WireType.VARINT, "int", "0"),
    FieldDescriptorProto.TYPE_INT32: ProtoTypeDescriptor("int32", WireType.VARINT, "int", "0"),
    FieldDescriptorProto.TYPE_INT64: ProtoTypeDescriptor("int64", WireType.VARINT, "int", "0"),
    FieldDescriptorProto.TYPE_UINT32: ProtoTypeDescriptor("uint32", WireType.VARINT, "int", "0"),
    FieldDescriptorProto.TYPE_UINT64: ProtoTypeDescriptor("uint64", WireType.VARINT, "int", "0"),
    FieldDescriptorProto.TYPE_SINT32: ProtoTypeDescriptor("sint32", WireType.VARINT, "int", "0"),
    FieldDescriptorProto.TYPE_SINT64: ProtoTypeDescriptor("sint64", WireType.VARINT, "int", "0"),
    FieldDescriptorProto.TYPE_FIXED32: ProtoTypeDescriptor("fixed32", WireType.I32, "int", "0"),
    FieldDescriptorProto.TYPE_FIXED64: ProtoTypeDescriptor("fixed64", WireType.I64, "int", "0"),
    FieldDescriptorProto.TYPE_SFIXED32: ProtoTypeDescriptor("sfixed32", WireType.I32, "int", "0"),
    FieldDescriptorProto.TYPE_SFIXED64: ProtoTypeDescriptor("sfixed64", WireType.I64, "int", "0"),
    FieldDescriptorProto.TYPE_FLOAT: ProtoTypeDescriptor("float", WireType.I32, "float", "0.0"),
    FieldDescriptorProto.TYPE_DOUBLE: ProtoTypeDescriptor("double", WireType.I64, "float", "0.0"),
    FieldDescriptorProto.TYPE_STRING: ProtoTypeDescriptor("string", WireType.LEN, "str", '""'),
    FieldDescriptorProto.TYPE_BYTES: ProtoTypeDescriptor("bytes", WireType.LEN, "bytes", 'b""'),
    FieldDescriptorProto.TYPE_MESSAGE: ProtoTypeDescriptor("message", WireType.LEN, "PLACEHOLDER", "None"),
}

@dataclass
class EnumValueTemplate:
    name: str
    number: int

    @staticmethod
    def from_descriptor(descriptor: EnumValueDescriptorProto) -> "EnumValueTemplate":
        return EnumValueTemplate(
            name=descriptor.name,
            number=descriptor.number,
        )

@dataclass
class EnumTemplate:
    name: str
    values: List["EnumValueTemplate"] = field(default_factory=list)

    @staticmethod
    def from_descriptor(descriptor: EnumDescriptorProto, parent: str = "") -> "EnumTemplate":
        return EnumTemplate(
            name=descriptor.name,
            values=[EnumValueTemplate.from_descriptor(value) for value in descriptor.value],
        )

def tag_to_repr_varint(tag: int) -> str:
    out = bytearray()
    while tag >= 128:
        out.append((tag & 0x7F) | 0x80)
        tag >>= 7
    out.append(tag)
    return repr(bytes(out))

@dataclass
class FieldTemplate:
    name: str
    number: int
    tag: str
    python_type: str
    proto_type: str
    repeated: bool
    group: str
    encode_presence: bool
    default_val: str

    @staticmethod
    def from_descriptor(descriptor: FieldDescriptorProto, group: Optional[str] = None) -> "FieldTemplate":
        repeated = descriptor.label == FieldDescriptorProto.LABEL_REPEATED
        type_descriptor = proto_type_to_descriptor[descriptor.type]

        python_type = type_descriptor.python_type
        proto_type = type_descriptor.name
        default_val = type_descriptor.default_val
        if proto_type == "message":
            python_type = re.sub(r"^[a-zA-Z0-9_\.]+\.v1\.", "", descriptor.type_name)

        if repeated:
            python_type = f"List[{python_type}]"
            proto_type = f"repeated_{proto_type}"
            default_val = "None"
        
        name = descriptor.name

        tag = (descriptor.number << 3) | type_descriptor.wire_type.value
        if repeated and type_descriptor.wire_type != WireType.LEN:
            # Special case: repeated primitive fields are packed
            # So we need to use the length-delimited wire type
            tag = (descriptor.number << 3) | WireType.LEN.value
        # Convert the tag to a varint representation
        # Saves us from having to calculate the tag at runtime
        tag = tag_to_repr_varint(tag)

        # For group / oneof fields, we need to encode the presence of the field
        # For message fields, we need to encode the presence of the field if it is not None
        encode_presence = group is not None or proto_type == "message"
        if group is not None:
            default_val = "None"

        return FieldTemplate(
            name=name,
            tag=tag,
            number=descriptor.number,
            python_type=python_type,
            proto_type=proto_type,
            repeated=repeated,
            group=group,
            encode_presence=encode_presence,
            default_val=default_val,
        )

@dataclass
class MessageTemplate:
    name: str
    fields: List[FieldTemplate] = field(default_factory=list)
    enums: List["EnumTemplate"] = field(default_factory=list)
    messages: List["MessageTemplate"] = field(default_factory=list)
    type_hints: List[str] = field(default_factory=list)

    @staticmethod
    def from_descriptor(descriptor: DescriptorProto, parent: str = "") -> "MessageTemplate":
        def get_group(field: FieldDescriptorProto) -> str:
            return descriptor.oneof_decl[field.oneof_index].name if field.HasField("oneof_index") else None
        fields = [FieldTemplate.from_descriptor(field, get_group(field)) for field in descriptor.field]
        fields.sort(key=lambda field: field.number)

        name = descriptor.name
        return MessageTemplate(
            name=name,
            fields=fields,
            enums=[EnumTemplate.from_descriptor(enum, name) for enum in descriptor.enum_type],
            messages=[MessageTemplate.from_descriptor(message, name) for message in descriptor.nested_type],
        )

@dataclass
class MethodTemplate:
    name: str
    input_message: MessageTemplate
    output_message: MessageTemplate

    @staticmethod
    def from_descriptor(descriptor: MethodDescriptorProto) -> "MethodTemplate":
        return MethodTemplate(
            name=descriptor.name,
            input_message=MessageTemplate(name=descriptor.input_type),
            output_message=MessageTemplate(name=descriptor.output_type),
        )

@dataclass
class ServiceTemplate:
    name: str
    methods: List["MethodTemplate"] = field(default_factory=list)

    @staticmethod
    def from_descriptor(descriptor: ServiceDescriptorProto) -> "ServiceTemplate":
        return ServiceTemplate(
            name=descriptor.name,
            methods=[MethodTemplate.from_descriptor(method) for method in descriptor.method],
        )

@dataclass
class FileTemplate:
    messages: List["MessageTemplate"] = field(default_factory=list)
    enums: List["EnumTemplate"] = field(default_factory=list)
    services: List["ServiceTemplate"] = field(default_factory=list)
    name: str = ""
    imports: List[str] = field(default_factory=list)

    @staticmethod
    def from_descriptor(descriptor: FileDescriptorProto) -> "FileTemplate":
        imports = []
        for dependency in descriptor.dependency:
            path = re.sub(r"/[a-zA-Z0-9_]+\.proto$", "", dependency)
            if descriptor.name.startswith(path):
                continue
            path = path.replace("/", ".")
            path = "snowflake.telemetry._internal." + path
            imports.append(path)

        return FileTemplate(
            messages=[MessageTemplate.from_descriptor(message) for message in descriptor.message_type],
            enums=[EnumTemplate.from_descriptor(enum) for enum in descriptor.enum_type],
            services=[ServiceTemplate.from_descriptor(service) for service in descriptor.service],
            imports=imports,
            name=descriptor.name,
        )

def main():
    request = plugin.CodeGeneratorRequest()
    request.ParseFromString(sys.stdin.buffer.read())

    response = plugin.CodeGeneratorResponse()
    # needed since metrics.proto uses proto3 optional fields
    response.supported_features = plugin.CodeGeneratorResponse.FEATURE_PROTO3_OPTIONAL

    template_env = Environment(loader=FileSystemLoader(f"{os.path.dirname(os.path.realpath(__file__))}/templates"))
    jinja_body_template = template_env.get_template("template.py.jinja2")

    for proto_file in request.proto_file:
        file_name = re.sub(r"[a-zA-Z0-9_]+\.proto$", "__init__.py", proto_file.name)
        file_descriptor_proto = proto_file

        file_template = FileTemplate.from_descriptor(file_descriptor_proto)

        code = jinja_body_template.render(file_template=file_template)
        code = isort.api.sort_code_string(
            code = code,
            show_diff=False,
            profile="black",
            combine_as_imports=True,
            lines_after_imports=2,
            quiet=True,
            force_grid_wrap=2,
        )
        code = black.format_str(
            src_contents=code,
            mode=black.Mode(),
        )

        response_file = response.file.add()
        response_file.name = file_name
        response_file.content = code

    sys.stdout.buffer.write(response.SerializeToString())

if __name__ == '__main__':
    main()
