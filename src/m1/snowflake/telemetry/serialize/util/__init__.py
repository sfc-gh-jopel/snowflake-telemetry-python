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

def size_bool(tag, _): return len(tag) + 1
def size_enum(tag, m): 
    if not isinstance(m, int):
        m = m.value
    return len(tag) + size_varint32(m)
def size_uint32(tag, m): return len(tag) + size_varint32(m)
def size_uint64(tag, m): return len(tag) + size_varint64(m)
def size_sint32(tag, m): return len(tag) + size_varint32(m << 1 if m >= 0 else (m << 1) ^ (~0))
def size_sint64(tag, m): return len(tag) + size_varint64(m << 1 if m >= 0 else (m << 1) ^ (~0))
def size_int32(tag, m): return len(tag) + size_varint32(m + 1 << 32 if m < 0 else m)
def size_int64(tag, m): return len(tag) + size_varint64(m + 1 << 64 if m < 0 else m)
def size_float(tag, _): return len(tag) + 4
def size_double(tag, _): return len(tag) + 8
def size_fixed32(tag, _): return len(tag) + 4
def size_fixed64(tag, _): return len(tag) + 8
def size_sfixed32(tag, _): return len(tag) + 4
def size_sfixed64(tag, _): return len(tag) + 8
def size_bytes(tag, m): return len(tag) + size_varint32(len(m)) + len(m)
def size_string(tag, m):
    # m = m.encode("utf-8") # TODO store this in the object to avoid encoding it twice
    return len(tag) + size_varint32(len(m)) + len(m)
def size_message(tag, m): 
    return len(tag) + size_varint32(m.size) + m.size
def size_repeated_message(tag, messages):
    return sum(message.size + len(tag) + size_varint32(message.size) for message in messages)
def size_repeated_double(tag, doubles): 
    return len(tag) + len(doubles) * 8 + size_varint32(len(doubles) * 8)
def size_repeated_fixed64(tag, fixed64s): 
    return len(tag) + len(fixed64s) * 8 + size_varint32(len(fixed64s) * 8)
def size_repeated_uint64(tag, uint32s):
    size = sum(size_varint64(uint32) for uint32 in uint32s)
    return len(tag) + size + size_varint32(size)
