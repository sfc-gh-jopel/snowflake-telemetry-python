import sys
import struct
import dataclasses
from abc import ABC
from io import BytesIO
from enum import IntEnum
from typing import Optional, Any, Callable, ClassVar, Dict, IO, Type, get_type_hints

def write_varint_unsigned(value: int, io: IO) -> None:
    if value < -(1 << 63):
        raise ValueError("Unable to encode vairnt within 10 bytes")
    elif value < 0:
        value += 1 << 64

    bits = value & 0x7F
    value >>= 7
    while value:
        io.write((0x80 | bits).to_bytes(1, "little"))
        bits = value & 0x7F
        value >>= 7
    io.write(bits.to_bytes(1, "little"))

def write_varint_zigzag(value: int, io: IO) -> None:
    write_varint_unsigned(value << 1 if value >= 0 else (value << 1) ^ (~0), io)

def write_varint_twoscompliment(value: int, io: IO) -> None:
    compliment = int.from_bytes(
        value.to_bytes(8, sys.byteorder, signed=True),
        sys.byteorder,
        signed=False,
    )
    write_varint_unsigned(compliment, io)

def write_bool(value: bool, io: IO) -> None:
    write_varint_unsigned(int(value), io)

def write_enum(value: Any, io: IO) -> None:
    if isinstance(value, int):
        write_varint_unsigned(value, io)
    else:
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

def write_message(value: "Message", io: IO) -> None:
    with BytesIO() as tmp_io:
        value.write_to(tmp_io)
        write_bytes(tmp_io.getvalue(), io)

def write_map(value: Any, io: IO) -> None:
    raise NotImplementedError("Map serialization is not implemented")

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

PLACEHOLDER = object()
def dataclass_field(
    number: int, 
    proto_type: TypeDescriptor, 
    group: Optional[str] = None, 
    optional: bool = False
) -> dataclasses.field:
    return dataclasses.field(
        default=None if optional else PLACEHOLDER,
        metadata={"magic": FieldMetaData(number, proto_type, group, optional)}
    )

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
class Message(ABC):
    __PROTOBUF_FIELDS_BY_NUMBER__: ClassVar[Dict[int, FieldMetaData]]
    __PROTOBUF_FIELDS_BY_NAME__: ClassVar[Dict[str, FieldMetaData]]
    __DEFAULT_VALUE_GEN_BY_NAME__: ClassVar[Dict[str, Callable[[], Any]]]
    __CURRENT_VALUE_BY_GROUP_NAME__: ClassVar[Dict[str, str]]

    @classmethod
    def _type_hint(cls, name: str) -> Type:
        return cls._type_hints()[name]

    @classmethod
    def _type_hints(cls) -> Dict[str, Type]:
        module = sys.modules[cls.__module__]
        return get_type_hints(cls, module.__dict__, {})

    def __post_init__(self) -> None:
        self.__PROTOBUF_FIELDS_BY_NUMBER__ = {}
        self.__PROTOBUF_FIELDS_BY_NAME__ = {}
        self.__DEFAULT_VALUE_GEN_BY_NAME__ = {}
        self.__CURRENT_VALUE_BY_GROUP_NAME__ = {}
        for field in dataclasses.fields(self):
            meta = FieldMetaData.get(field)
            self.__PROTOBUF_FIELDS_BY_NUMBER__[meta.number] = (field.name, meta)
            self.__PROTOBUF_FIELDS_BY_NAME__[field.name] = meta

            # Keep track of which value is set for oneof fields
            value = self._raw_get(field.name)
            if value is not PLACEHOLDER or (not meta.optional and value is None):
                if meta.group:
                    self.__CURRENT_VALUE_BY_GROUP_NAME__[meta.group] = field.name

            # https://protobuf.dev/programming-guides/proto3/#default
            type = self._type_hint(field.name)
            if hasattr(type, "__origin__") and type.__origin__ is list:
                # empty list for repeated fields
                self.__DEFAULT_VALUE_GEN_BY_NAME__[field.name] = list
            elif hasattr(type, "__origin__") and type.__origin__ is dict:
                # empty dict for map fields
                self.__DEFAULT_VALUE_GEN_BY_NAME__[field.name] = dict
            elif issubclass(type, Enum):
                # enums default to 0 enumeral value
                self.__DEFAULT_VALUE_GEN_BY_NAME__[field.name] = lambda type=type: type._value2member_map_[0]
            elif issubclass(type, Message):
                # default to None for message fields
                self.__DEFAULT_VALUE_GEN_BY_NAME__[field.name] = lambda: None
            else:
                # primitive scalar, default to zero value
                # str, bytes, float, int, bool
                self.__DEFAULT_VALUE_GEN_BY_NAME__[field.name] = type
    
    # Write serialized protobuf message to io stream
    def write_to(self, io: IO) -> None:
        for _, (name, meta) in self.__PROTOBUF_FIELDS_BY_NUMBER__.items():
            try:
                value = getattr(self, name)
            except AttributeError:
                continue
            if value is None:
                continue

            # https://protobuf.dev/programming-guides/proto3/#default
            # if the value is the default value for the field, skip it
            default_value = self.__DEFAULT_VALUE_GEN_BY_NAME__[name]()
            if value == default_value:
                continue

            # repeated fields
            if isinstance(value, list):
                if meta.proto_type.packed:
                    # packed repeated fields are untagged and treated as a byte array
                    with BytesIO() as buf:
                        for item in value:
                            meta.proto_type.write(item, buf)
                        write_bytes(buf.getvalue(), io)
                else:
                    # unpacked repeated fields are each individually tagged
                    for item in value:
                        write_tag(meta.number, meta.proto_type.wire_type, io)
                        meta.proto_type.write(item, io)
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

    def __getattribute__(self, name: str) -> Any:
        """
        Lazy initialization of fields default values
        Raise :class:`AttributeError` if a field in a group is already set
        """
        value = super().__getattribute__(name)
        if value is not PLACEHOLDER:
            return value
        
        meta = super().__getattribute__("__PROTOBUF_FIELDS_BY_NAME__")[name]
        if meta.group:
            current_value = super().__getattribute__("__CURRENT_VALUE_BY_GROUP_NAME__").get(meta.group)
            if current_value and current_value != name:
                raise AttributeError(f"Only one field in group '{meta.group}' can be set")
        
        default_value_gen = super().__getattribute__("__DEFAULT_VALUE_GEN_BY_NAME__")[name]
        value = default_value_gen()
        setattr(self, name, value)
        return value
    
    def _raw_get(self, name: str) -> Any:
        return super().__getattribute__(name)
