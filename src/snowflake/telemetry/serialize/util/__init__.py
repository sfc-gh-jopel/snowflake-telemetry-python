def size_varint(value: int) -> int:
    size = 1
    while value >= 128:
        size += 1
        value >>= 7
    return size

def size_varint_signed(value: int) -> int:
    if value < 0:
        value += 1 << 64
    return size_varint(value)

def size_varint_zz(value: int) -> int:
    return size_varint(value << 1 if value >= 0 else (value << 1) ^ (~0))

size_bool = lambda tag, _: len(tag) + 1
size_enum = lambda tag, m: len(tag) + size_varint(m)
size_uint32 = lambda tag, m: len(tag) + size_varint(m)
size_uint64 = lambda tag, m: len(tag) + size_varint(m)
size_sint32 = lambda tag, m: len(tag) + size_varint_zz(m)
size_sint64 = lambda tag, m: len(tag) + size_varint_zz(m)
size_int32 = lambda tag, m: len(tag) + size_varint_signed(m)
size_int64 = lambda tag, m: len(tag) + size_varint_signed(m)
size_float = lambda tag, _: len(tag) + 4
size_double = lambda tag, _: len(tag) + 8
size_fixed32 = lambda tag, _: len(tag) + 4
size_fixed64 = lambda tag, _: len(tag) + 8
size_sfixed32 = lambda tag, _: len(tag) + 4
size_sfixed64 = lambda tag, _: len(tag) + 8
size_bytes = lambda tag, m: len(tag) + size_varint(len(m)) + len(m)
size_string = lambda tag, m: len(tag) + size_varint(len(m)) + len(m)
size_message = lambda tag, m: len(tag) + size_varint(m.size) + m.size

size_repeated_message = lambda tag, messages: sum(message.size + len(tag) + size_varint(message.size) for message in messages)
size_repeated_double = lambda tag, doubles: len(tag) + len(doubles) * 8 + size_varint(len(doubles) * 8)
size_repeated_fixed64 = lambda tag, fixed64s: len(tag) + len(fixed64s) * 8 + size_varint(len(fixed64s) * 8)
def size_repeated_uint64(tag, uint32s):
    size = sum(size_varint(uint32) for uint32 in uint32s)
    return len(tag) + size + size_varint(size)
