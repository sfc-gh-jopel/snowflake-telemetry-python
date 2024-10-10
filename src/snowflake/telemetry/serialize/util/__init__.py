def size_varint32(value: int) -> int:
    if (value & (0xffffffff << 7)) == 0:
        return 1
    if (value & (0xffffffff << 14)) == 0:
        return 2
    if (value & (0xffffffff << 21)) == 0:
        return 3
    if (value & (0xffffffff << 28)) == 0:
        return 4
    return 5

def size_varint64(value: int) -> int:
    if (value & (0xffffffffffffffff << 7)) == 0:
        return 1
    if (value < 0):
        return 10
    n = 2
    if (value & (0xffffffffffffffff << 35)) != 0:
        n += 4
        value >>= 28
    if (value & (0xffffffffffffffff << 21)) != 0:
        n += 2
        value >>= 14
    if (value & (0xffffffffffffffff << 14)) != 0:
        n += 1
    return n

size_bool = lambda tag, _: len(tag) + 1
size_enum = lambda tag, m: len(tag) + size_varint32(m)
size_uint32 = lambda tag, m: len(tag) + size_varint32(m)
size_uint64 = lambda tag, m: len(tag) + size_varint64(m)
size_sint32 = lambda tag, m: len(tag) + size_varint32(m << 1 if m >= 0 else (m << 1) ^ (~0))
size_sint64 = lambda tag, m: len(tag) + size_varint64(m << 1 if m >= 0 else (m << 1) ^ (~0))
size_int32 = lambda tag, m: len(tag) + size_varint32(m + 1 << 32 if m < 0 else m)
size_int64 = lambda tag, m: len(tag) + size_varint64(m + 1 << 64 if m < 0 else m)
size_float = lambda tag, _: len(tag) + 4
size_double = lambda tag, _: len(tag) + 8
size_fixed32 = lambda tag, _: len(tag) + 4
size_fixed64 = lambda tag, _: len(tag) + 8
size_sfixed32 = lambda tag, _: len(tag) + 4
size_sfixed64 = lambda tag, _: len(tag) + 8
size_bytes = lambda tag, m: len(tag) + size_varint32(len(m)) + len(m)
def size_string(tag, m):
    m = m.encode("utf-8") # TODO store this in the object, quite big speedup
    return len(tag) + size_varint32(len(m)) + len(m)
size_message = lambda tag, m: len(tag) + size_varint32(m.size) + m.size

size_repeated_message = lambda tag, messages: sum(message.size + len(tag) + size_varint32(message.size) for message in messages)
size_repeated_double = lambda tag, doubles: len(tag) + len(doubles) * 8 + size_varint32(len(doubles) * 8)
size_repeated_fixed64 = lambda tag, fixed64s: len(tag) + len(fixed64s) * 8 + size_varint32(len(fixed64s) * 8)
def size_repeated_uint64(tag, uint32s):
    size = sum(size_varint64(uint32) for uint32 in uint32s)
    return len(tag) + size + size_varint32(size)
