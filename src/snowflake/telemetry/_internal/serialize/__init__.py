from __future__ import annotations

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

Enum = IntEnum

class MessageMarshaler:
    def write_to(self, proto_serializer: ProtoSerializer) -> None:
        ...
    
    def calculate_size(self) -> int:
        ...

    def _get_size(self) -> int:
        if not hasattr(self, "_size"):
            self._size = self.calculate_size()
        return self._size
    
    def __bytes__(self) -> bytes:
        serializer = ProtoSerializer(self._get_size())
        self.write_to(serializer)
        return bytes(serializer)
    
    def SerializeToString(self) -> bytes:
        return bytes(self)

class ProtoSerializer:
    def __init__(self, size) -> None:
        self.out = BytesIO(initial_bytes=b"\0" * size)
        self.out.seek(0)

    def __bytes__(self) -> bytes:
        return self.out.getvalue()
    
    def __exit__(self, *args) -> None:
        self.out.close()

    def _write_varint_unsigned(self, value: int) -> None:
        while value >= 128:
            self.out.write(((value & 0x7F) | 0x80).to_bytes(1, "little"))
            value >>= 7
        self.out.write(value.to_bytes(1, "little"))
