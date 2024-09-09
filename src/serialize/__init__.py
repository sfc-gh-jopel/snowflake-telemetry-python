import struct
import dataclasses
from abc import ABC
from io import BytesIO
from enum import IntEnum
from sys import byteorder
from typing import Optional, Any, Callable, ClassVar, Dict, IO

# overwrite enum
Enum = IntEnum

# https://protobuf.dev/programming-guides/encoding/#structure
class WireType(IntEnum):
    VARINT = 0
    I64 = 1
    LEN = 2
    I32 = 5

"""
Dataclass holding information on how to serialize a protobuf field
based on its type
"""
@dataclasses.dataclass
class TypeDescriptor:
    wire_type: 'WireType'
    write: Callable[[Any, IO], None]
    packed: bool = False # efficiently encoded when it is a repeated field

def write_varint_unsigned(value: int, io: IO) -> None:
    while value > 0x7F:
        io.write(bytes((value & 0x7F | 0x80,)))
        value >>= 7
    io.write(bytes((value,)))

def write_varint_zigzag(value: int, io: IO) -> None:
    write_varint_unsigned(abs(value) * 2 - (value < 0), io)

def write_varint_twoscompliment(value: int, io: IO) -> None:
    compliment = int.from_bytes(
        value.to_bytes(8, byteorder, signed=True),
        byteorder,
        signed=False,
    )
    write_varint_unsigned(compliment, io)

def write_bool(value: bool, io: IO) -> None:
    write_varint_unsigned(int(value), io)

def write_enum(value: Any, io: IO) -> None:
    write_varint_unsigned(value.value, io)

class WriteStruct:
    def __init__(self, fmt) -> None:
        self.fmt = fmt

    def __call__(self, value: Any, io: IO) -> None:
        io.write(struct.pack(self.fmt, value))

def write_string(value: str, io: IO) -> None:
    write_bytes(value.encode("utf-8"), io)

def write_bytes(value: bytes, io: IO) -> None:
    write_varint_unsigned(len(value), io)
    io.write(value)

def write_message(value: "BaseMessage", io: IO) -> None:
    with BytesIO() as tmp_io:
        value.write_to(tmp_io)
        write_bytes(tmp_io.getvalue(), io)

def write_map(value: Any, io: IO) -> None:
    raise NotImplementedError("Map serialization is not implemented")

TYPE_ENUM = TypeDescriptor(WireType.VARINT, write_enum, packed=True)

TYPE_BOOL = TypeDescriptor(WireType.VARINT, write_bool, packed=True)

TYPE_INT32 = TypeDescriptor(WireType.VARINT, write_varint_twoscompliment, packed=True)

TYPE_INT64 = TypeDescriptor(WireType.VARINT, write_varint_twoscompliment, packed=True)

TYPE_UINT32 = TypeDescriptor(WireType.VARINT, write_varint_unsigned, packed=True)

TYPE_UINT64 = TypeDescriptor(WireType.VARINT, write_varint_unsigned, packed=True)

TYPE_SINT32 = TypeDescriptor(WireType.VARINT, write_varint_zigzag, packed=True)

TYPE_SINT64 = TypeDescriptor(WireType.VARINT, write_varint_zigzag, packed=True)

TYPE_FLOAT = TypeDescriptor(WireType.I32, WriteStruct("<f"), packed=True)

TYPE_DOUBLE = TypeDescriptor(WireType.I64, WriteStruct("<d"), packed=True)

TYPE_FIXED32 = TypeDescriptor(WireType.I32, WriteStruct("<I"), packed=True)

TYPE_SFIXED32 = TypeDescriptor(WireType.I32, WriteStruct("<i"), packed=True)

TYPE_FIXED64 = TypeDescriptor(WireType.I64, WriteStruct("<Q"), packed=True)

TYPE_SFIXED64 = TypeDescriptor(WireType.I64, WriteStruct("<q"), packed=True)

TYPE_STRING = TypeDescriptor(WireType.LEN, write_string, packed=False)

TYPE_BYTES = TypeDescriptor(WireType.LEN, write_bytes, packed=False)

TYPE_MESSAGE = TypeDescriptor(WireType.LEN, write_message, packed=False)

TYPE_MAP = TypeDescriptor(WireType.LEN, write_map, packed=False)

"""
Dataclass holding metadata about a protobuf field
""" 
@dataclasses.dataclass(frozen=True)
class FieldMetaData:
    number: int
    proto_type: TypeDescriptor
    group: Optional[str] # group name if this field is part of a 'oneof' group
    optional: bool = False

    @staticmethod
    def get(field: dataclasses.field) -> "FieldMetaData":
        return field.metadata["magic"]

def dataclass_field(
    number: int, 
    proto_type: TypeDescriptor, 
    group: Optional[str] = None, 
    optional: bool = False
) -> dataclasses.field:
    return dataclasses.field(metadata={"magic": FieldMetaData(number, proto_type, group, optional)})

def enum_field(number: int, group: Optional[str] = None, optional: bool = False) -> Any:
    return dataclass_field(number, TYPE_ENUM, group=group, optional=optional)

def bool_field(number: int, group: Optional[str] = None, optional: bool = False) -> Any:
    return dataclass_field(number, TYPE_BOOL, group=group, optional=optional)

def int32_field(number: int, group: Optional[str] = None, optional: bool = False) -> Any:
    return dataclass_field(number, TYPE_INT32, group=group, optional=optional)

def int64_field(number: int, group: Optional[str] = None, optional: bool = False) -> Any:
    return dataclass_field(number, TYPE_INT64, group=group, optional=optional)

def uint32_field(number: int, group: Optional[str] = None, optional: bool = False) -> Any:
    return dataclass_field(number, TYPE_UINT32, group=group, optional=optional)

def uint64_field(number: int, group: Optional[str] = None, optional: bool = False) -> Any:
    return dataclass_field(number, TYPE_UINT64, group=group, optional=optional)

def sint32_field(number: int, group: Optional[str] = None, optional: bool = False) -> Any:
    return dataclass_field(number, TYPE_SINT32, group=group, optional=optional)

def sint64_field(number: int, group: Optional[str] = None, optional: bool = False) -> Any:
    return dataclass_field(number, TYPE_SINT64, group=group, optional=optional)

def float_field(number: int, group: Optional[str] = None, optional: bool = False) -> Any:
    return dataclass_field(number, TYPE_FLOAT, group=group, optional=optional)

def double_field(number: int, group: Optional[str] = None, optional: bool = False) -> Any:
    return dataclass_field(number, TYPE_DOUBLE, group=group, optional=optional)

def fixed32_field(number: int, group: Optional[str] = None, optional: bool = False) -> Any:
    return dataclass_field(number, TYPE_FIXED32, group=group, optional=optional)

def fixed64_field(number: int, group: Optional[str] = None, optional: bool = False) -> Any:
    return dataclass_field(number, TYPE_FIXED64, group=group, optional=optional)

def sfixed32_field(number: int, group: Optional[str] = None, optional: bool = False) -> Any:
    return dataclass_field(number, TYPE_SFIXED32, group=group, optional=optional)

def sfixed64_field(number: int, group: Optional[str] = None, optional: bool = False) -> Any:
    return dataclass_field(number, TYPE_SFIXED64, group=group, optional=optional)

def string_field(number: int, group: Optional[str] = None, optional: bool = False) -> Any:
    return dataclass_field(number, TYPE_STRING, group=group, optional=optional)

def bytes_field(number: int, group: Optional[str] = None, optional: bool = False) -> Any:
    return dataclass_field(number, TYPE_BYTES, group=group, optional=optional)

def message_field(number: int, group: Optional[str] = None, optional: bool = False,) -> Any:
    return dataclass_field(number, TYPE_MESSAGE, group=group, optional=optional)

# Helpers for serializing fields
def write_tag(number: int, wire_type: WireType, io: IO) -> None:
    write_varint_unsigned((number << 3) | wire_type, io)

"""
Abstract class for protobuf messages.
All protobuf message objects should inherit from this class.
"""
class BaseMessage(ABC):
    __PROTOBUF_FIELDS_BY_NUMBER__: ClassVar[Dict[int, FieldMetaData]]
    __PROTOBUF_FIELDS_BY_NAME__: ClassVar[Dict[str, FieldMetaData]]

    def __init_subclass__(cls) -> None:
        cls.__PROTOBUF_FIELDS_BY_NUMBER__ = {}
        cls.__PROTOBUF_FIELDS_BY_NAME__ = {}
        for field in dataclasses.fields(cls):
            meta = FieldMetaData.get(field)
            cls.__PROTOBUF_FIELDS_BY_NUMBER__[meta.number] = (field.name, meta)
            cls.__PROTOBUF_FIELDS_BY_NAME__[field.name] = meta
    
    # Write serialized protobuf message to io stream
    def write_to(self, io: IO) -> None:
        for _, (name, meta) in self.__PROTOBUF_FIELDS_BY_NUMBER__.items():
            value = getattr(self, name)
            # repeated fields
            if isinstance(value, list):
                if meta.packed:
                    # packed repeated fields are untagged and treated as a byte array
                    with BytesIO as buf:
                        for item in value:
                            meta.proto_type.write(item, buf)
                        write_bytes(buf.getvalue(), io)
                else:
                    # unpacked repeated fields are each individually tagged
                    with BytesIO as buf:
                        for item in value:
                            write_tag(meta.number, meta.proto_type.wire_type, buf)
                            meta.proto_type.write(item, buf)
                        io.write(buf.getvalue())
            else:
                write_tag(meta.number, meta.proto_type.wire_type, io)
                meta.proto_type.write(value, io)
    
    # Serialize message to bytes
    def __bytes__(self) -> bytes:
        with BytesIO() as io:
            self.write_to(io)
            return io.getvalue()
    
    # For compatibility with protoc compiled python classes
    # Alias for bytes(self)
    def SerializeToString(self) -> bytes:
        return bytes(self)
