from __future__ import annotations

import struct
from enum import IntEnum
from io import BytesIO

def size_varint32(value: int) -> int:
    size = 1
    while value >= 128:
        value >>= 7
        size += 1
    return size

def size_varint64(value: int) -> int:
    size = 1
    while value >= 128:
        value >>= 7
        size += 1
    return size

def write_varint_unsigned(out: BytesIO, value: int) -> None:
    while value >= 128:
        out.write(struct.pack("B", value & 0x7F | 0x80))
        value >>= 7
    out.write(struct.pack("B", value))

Enum = IntEnum

class MessageMarshaler:
    def write_to(self, out: BytesIO) -> None:
        ...
    
    def calculate_size(self) -> int:
        ...

    def _get_size(self) -> int:
        if not hasattr(self, "_size"):
            self._size = self.calculate_size()
        return self._size
    
    def __bytes__(self) -> bytes:
        with BytesIO(initial_bytes=b"\0" * self._get_size()) as stream:
            self.write_to(stream)
            return stream.getvalue()
    
    def SerializeToString(self) -> bytes:
        with BytesIO(initial_bytes=b"\0" * self._get_size()) as stream:
            self.write_to(stream)
            return stream.getvalue()
