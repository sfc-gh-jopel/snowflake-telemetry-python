import struct
from enum import IntEnum
from typing import Callable, Any, List, Union

Enum = IntEnum

class MessageMarshaler:
    def __bytes__(self) -> bytes:
        out = ProtoSerializer()
        self.write_to(out)
        return bytes(out)

    def write_to(self, out: "ProtoSerializer") -> None:
        ...

class ProtoSerializer:
    __slots__ = ("out","buf","i")

    def __init__(self) -> None:
        self.i = 1024
        self.out = bytearray(self.i)
        self.buf = memoryview(self.out)
    
    def __bytes__(self) -> bytes:
        return bytes(self.out[self.i:])
    
    def make_room(self, size: int) -> None:
        if self.i < size:
            self.buf.release()
            inc = max(len(self.out), size)
            self.out = bytearray(inc) + self.out
            self.buf = memoryview(self.out)
            self.i += inc

    def serialize_bool(self, tag: bytes, value: bool) -> None:
        self.make_room(1 + len(tag))
        self._write_varint_unsigned(1 if value else 0)
        self.buf[self.i-len(tag):self.i] = tag
        self.i -= len(tag)
    
    def serialize_enum(self, tag: bytes, value: Union[Enum, int]) -> None:
        if not isinstance(value, int):
            value = value.value
        self.make_room(10 + len(tag))
        self._write_varint_unsigned(value)
        self.buf[self.i-len(tag):self.i] = tag
        self.i -= len(tag)
    
    def serialize_uint32(self, tag: bytes, value: int) -> None:
        self.make_room(5 + len(tag))
        self._write_varint_unsigned(value)
        self.buf[self.i-len(tag):self.i] = tag
        self.i -= len(tag)
    
    def serialize_uint64(self, tag: bytes, value: int) -> None:
        self.make_room(10 + len(tag))
        self._write_varint_unsigned(value)
        self.buf[self.i-len(tag):self.i] = tag
        self.i -= len(tag)
    
    def serialize_sint32(self, tag: bytes, value: int) -> None:
        self.make_room(5 + len(tag))
        self._write_varint_unsigned(encode_zigzag32(value))
        self.buf[self.i-len(tag):self.i] = tag
        self.i -= len(tag)
    
    def serialize_sint64(self, tag: bytes, value: int) -> None:
        self.make_room(10 + len(tag))
        self._write_varint_unsigned(encode_zigzag64(value))
        self.buf[self.i-len(tag):self.i] = tag
        self.i -= len(tag)
    
    def serialize_int32(self, tag: bytes, value: int) -> None:
        self.make_room(5 + len(tag))
        self._write_varint_signed(value)
        self.buf[self.i-len(tag):self.i] = tag
        self.i -= len(tag)
    
    def serialize_int64(self, tag: bytes, value: int) -> None:
        self._write_varint_signed(value)
        self.make_room(len(tag))
        self.buf[self.i-len(tag):self.i] = tag
        self.i -= len(tag)
    
    def serialize_fixed32(self, tag: bytes, value: int) -> None:
        self.make_room(4 + len(tag))
        self.buf[self.i-4:self.i] = struct.pack("<I", value)
        self.i -= 4
        self.buf[self.i-len(tag):self.i] = tag
        self.i -= len(tag)
    
    def serialize_fixed64(self, tag: bytes, value: int) -> None:
        self.make_room(8 + len(tag))
        self.buf[self.i-8:self.i] = struct.pack("<Q", value)
        self.i -= 8
        self.buf[self.i-len(tag):self.i] = tag
        self.i -= len(tag)
    
    def serialize_sfixed32(self, tag: bytes, value: int) -> None:
        self.make_room(4 + len(tag))
        self.buf[self.i-4:self.i] = struct.pack("<i", value)
        self.i -= 4
        self.buf[self.i-len(tag):self.i] = tag
        self.i -= len(tag)
    
    def serialize_sfixed64(self, tag: bytes, value: int) -> None:
        self.make_room(8 + len(tag))
        self.buf[self.i-8:self.i] = struct.pack("<q", value)
        self.i -= 8
        self.buf[self.i-len(tag):self.i] = tag
        self.i -= len(tag)
    
    def serialize_float(self, tag: bytes, value: float) -> None:
        self.make_room(4 + len(tag))
        self.buf[self.i-4:self.i] = struct.pack("<f", value)
        self.i -= 4
        self.buf[self.i-len(tag):self.i] = tag
        self.i -= len(tag)
    
    def serialize_double(self, tag: bytes, value: float) -> None:
        self.make_room(8 + len(tag))
        self.buf[self.i-8:self.i] = struct.pack("<d", value)
        self.i -= 8
        self.buf[self.i-len(tag):self.i] = tag
        self.i -= len(tag)
    
    def serialize_bytes(self, tag: bytes, value: bytes) -> None:
        self.make_room(len(value) + 10 + len(tag))
        self.buf[self.i-len(value):self.i] = value
        self.i -= len(value)
        self._write_varint_unsigned(len(value))
        self.buf[self.i-len(tag):self.i] = tag
        self.i -= len(tag)
    
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
        before = len(self.out) - self.i
        value.write_to(self)
        after = len(self.out) - self.i
        # Need to make room after the message was written
        self.make_room(10 + len(tag))
        self._write_varint_unsigned(after - before)
        self.buf[self.i-len(tag):self.i] = tag
        self.i -= len(tag)

    def serialize_repeated_message(
            self, 
            tag: bytes, 
            values: List[MessageMarshaler],
        ) -> None:
        if not values:
            return
        # local reference to avoid repeated lookups
        _self_serialize = self.serialize_message
        for value in reversed(values):
            _self_serialize(tag, value)
    
    def serialize_repeated_packed(
            self, 
            tag: bytes, 
            values: List[Any],
            write_value: Callable[[Any, bytearray], None],
        ) -> None:
        if not values:
            return
        # Packed repeated fields are encoded like a bytearray
        # with a total size prefix and a single tag
        # (similar to a bytes field)
        before = len(self.out) - self.i
        for value in reversed(values):
            write_value(value)
        after = len(self.out) - self.i
        self.make_room(10 + len(tag))
        self._write_varint_unsigned(after - before)
        self.buf[self.i-len(tag):self.i] = tag
        self.i -= len(tag)
    
    def serialize_repeated_double(self, tag: bytes, values: List[float]) -> None:
        self.make_room(8 * len(values))
        self.serialize_repeated_packed(tag, values, self.write_double_no_tag)
    
    def serialize_repeated_fixed64(self, tag: bytes, values: List[int]) -> None:
        self.make_room(8 * len(values))
        self.serialize_repeated_packed(tag, values, self.write_fixed64_no_tag)
    
    def serialize_repeated_uint64(self, tag: bytes, values: List[int]) -> None:
        self.serialize_repeated_packed(tag, values, self._write_varint_unsigned_make_room)
    
    def _write_varint_unsigned_make_room(self, value: int) -> None:
        l = size_varint(value)
        self.make_room(l)
        j = self.i - l
        while value >= 128:
            self.buf[j] = (value & 0x7F) | 0x80
            j += 1
            value >>= 7
        self.buf[j] = value
        self.i -= l

    # For methods below, responsibility of caller to write tage and ensure enough space in buffer
    def _write_varint_signed(self, value: int) -> None:
        if value < 0:
            value += 1 << 64
        self._write_varint_unsigned(value)

    def _write_varint_unsigned(self, value: int) -> None:
        l = size_varint(value)
        j = self.i - l
        while value >= 128:
            self.buf[j] = (value & 0x7F) | 0x80
            j += 1
            value >>= 7
        self.buf[j] = value
        self.i -= l

    def write_double_no_tag(self, value: float) -> None:
        self.buf[self.i-8:self.i] = struct.pack("<d", value)
        self.i -= 8

    def write_fixed64_no_tag(self, value: int) -> None:
        self.buf[self.i-8:self.i] = struct.pack("<Q", value)
        self.i -= 8

def size_varint(value: int) -> int:
    size = 1
    while value >= 128:
        size += 1
        value >>= 7
    return size

def encode_zigzag32(value: int) -> int:
    return value << 1 if value >= 0 else (value << 1) ^ (~0)

def encode_zigzag64(value: int) -> int:
    return value << 1 if value >= 0 else (value << 1) ^ (~0)
