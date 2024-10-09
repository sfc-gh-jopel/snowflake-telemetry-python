import struct
from enum import IntEnum
from typing import Callable, Any, List, Union

from snowflake.telemetry.serialize.util import (
    size_varint,
    size_repeated_double,
    size_repeated_fixed64,
    size_repeated_uint64,
)

Enum = IntEnum

class MessageMarshaler:
    def __init__(self, size: int) -> None:
        self.size = size

    def __bytes__(self) -> bytes:
        out = ProtoSerializer()
        self.write_to(out)
        return bytes(out)

    def write_to(self, out: "ProtoSerializer") -> None:
        ...

class ProtoSerializer:
    __slots__ = ("out","varint_buf")

    def __init__(self) -> None:
        self.out = bytearray()
        self.varint_buf = memoryview(bytearray(10))
    
    def __bytes__(self) -> bytes:
        return bytes(self.out)
    
    def serialize_bool(self, tag: bytes, value: bool) -> None:
        self.out += tag
        self._write_varint_unsigned(1 if value else 0)
    
    def serialize_enum(self, tag: bytes, value: Union[Enum, int]) -> None:
        if not isinstance(value, int):
            value = value.value
        self.out += tag
        self._write_varint_unsigned(value)
    
    def serialize_uint32(self, tag: bytes, value: int) -> None:
        self.out += tag
        self._write_varint_unsigned(value)
    
    def serialize_uint64(self, tag: bytes, value: int) -> None:
        self.out += tag
        self._write_varint_unsigned(value)
    
    def serialize_sint32(self, tag: bytes, value: int) -> None:
        self.out += tag
        self._write_varint_unsigned(encode_zigzag32(value))
    
    def serialize_sint64(self, tag: bytes, value: int) -> None:
        self.out += tag
        self._write_varint_unsigned(encode_zigzag64(value))
    
    def serialize_int32(self, tag: bytes, value: int) -> None:
        self.out += tag
        self._write_varint_signed(value)
    
    def serialize_int64(self, tag: bytes, value: int) -> None:
        self.out += tag
        self._write_varint_signed(value)
    
    def serialize_fixed32(self, tag: bytes, value: int) -> None:
        self.out += tag
        self.out += struct.pack("<I", value)
    
    def serialize_fixed64(self, tag: bytes, value: int) -> None:
        self.out += tag
        self.out += struct.pack("<Q", value)
    
    def serialize_sfixed32(self, tag: bytes, value: int) -> None:
        self.out += tag
        self.out += struct.pack("<i", value)
    
    def serialize_sfixed64(self, tag: bytes, value: int) -> None:
        self.out += tag
        self.out += struct.pack("<q", value)
    
    def serialize_float(self, tag: bytes, value: float) -> None:
        self.out += tag
        self.out += struct.pack("<f", value)
    
    def serialize_double(self, tag: bytes, value: float) -> None:
        self.out += tag
        self.out += struct.pack("<d", value)
    
    def serialize_bytes(self, tag: bytes, value: bytes) -> None:
        self.out += tag
        self._write_varint_unsigned(len(value))
        self.out += value
    
    def serialize_string(self, tag: bytes, value: str) -> None:
        self.serialize_bytes(tag, value.encode("utf-8"))

    def serialize_message(
            self, 
            tag: bytes, 
            value: MessageMarshaler,
        ) -> None:
        # If value is None, omit message entirely
        if value is None:
            return
        # Otherwise, write the message
        # Even if all fields are default (ommnited)
        # The presence of the message is still encoded
        self.out += tag
        self._write_varint_unsigned(value.size)
        value.write_to(self)

    def serialize_repeated_message(
            self, 
            tag: bytes, 
            values: List[MessageMarshaler],
        ) -> None:
        if not values:
            return
        # local reference to avoid repeated lookups
        _self_serialize = self.serialize_message
        for value in values:
            _self_serialize(tag, value)
    
    def serialize_repeated_packed(
            self, 
            tag: bytes, 
            values: List[Any],
            write_value: Callable[[Any, bytearray], None],
            size_values: Callable[[Any], int],
        ) -> None:
        if not values:
            return
        # Packed repeated fields are encoded like a bytearray
        # with a total size prefix and a single tag
        # (similar to a bytes field)
        self.out += tag
        self._write_varint_unsigned(size_values(values)) # TODO: this size includes the tag
        for value in values:
            write_value(value)
    
    def serialize_repeated_double(self, tag: bytes, values: List[float]) -> None:
        self.serialize_repeated_packed(tag, values, self.write_double_no_tag, size_repeated_double)
    
    def serialize_repeated_fixed64(self, tag: bytes, values: List[int]) -> None:
        self.serialize_repeated_packed(tag, values, self.write_fixed64_no_tag, size_repeated_fixed64)
    
    def serialize_repeated_uint64(self, tag: bytes, values: List[int]) -> None:
        self.serialize_repeated_packed(tag, values, self._write_varint_unsigned, size_repeated_uint64)

    def _write_varint_signed(self, value: int) -> None:
        if value < 0:
            value += 1 << 64
        self._write_varint_unsigned(value)

    def _write_varint_unsigned(self, value: int) -> None:
        j = 0
        while value >= 128:
            self.varint_buf[j] = (value & 0x7F) | 0x80
            j += 1
            value >>= 7
        self.varint_buf[j] = value
        j += 1
        self.out += self.varint_buf[:j]

    def write_double_no_tag(self, value: float) -> None:
        self.out += struct.pack("<d", value)

    def write_fixed64_no_tag(self, value: int) -> None:
        self.out += struct.pack("<Q", value)

def encode_zigzag32(value: int) -> int:
    return value << 1 if value >= 0 else (value << 1) ^ (~0)

def encode_zigzag64(value: int) -> int:
    return value << 1 if value >= 0 else (value << 1) ^ (~0)
