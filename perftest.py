# 
# WRITING TO BUFFER BENCHMARKS
# 

def bm_presize_bytearray_memoryview():
    b = bytearray(len(b"hello world") * 10000)
    m = memoryview(b)
    i = 0
    l = len(b"hello world")
    for _ in range(10000):
        m[i:i+l] = b"hello world"
        i += l
    return b

def bm_presize_bytearray():
    b = bytearray(len(b"hello world") * 10000)
    i = 0
    l = len(b"hello world")
    for _ in range(10000):
        b[i:i+l] = b"hello world"
        i += l
    return b

def bm_bytearray_extend():
    b = bytearray()
    for _ in range(10000):
        b.extend(b"hello world")
    return b

def bm_bytearray_plus():
    b = bytearray()
    for _ in range(10000):
        b += b"hello world"
    return b

def bm_bytearray_plus_reverse():
    b = bytearray()
    for _ in range(10000):
        b += b"hello world"[::-1]
    return b[::-1]

from io import BytesIO
def bm_BytesIO():
    b = BytesIO()
    for _ in range(10000):
        b.write(b"hello world")
    return b.getvalue()

import ctypes
def bm_ctypes_string_buffer():
    cpy_string = b"hello world"
    l = len(cpy_string)
    b = ctypes.create_string_buffer(l * 10000)
    j = 0
    for i in range(10000):
        ctypes.memmove(ctypes.byref(b, j), cpy_string, l)
        j += l
    return b.raw

# 
# OBJECT INSTANTIATION BENCHMARKS
# 

from typing import TypedDict
class Msg(TypedDict):
    name: str
    age: int

class Msg2:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

def bm_TypedDict():
    for _ in range(10000):
        Msg(name="hello world", age=100)

def bm_class_vanilla_obj():
    for _ in range(10000):
        Msg2(name="hello world", age=100)

def create_dict(name: str, age: int) -> dict:
    return {"name": name, "age": age}

def bm_vanilla_dict():
    for _ in range(10000):
        create_dict("hello world", 100)

def bm_pass_function_to_caller():
    def dummy(name: str, age: int) -> None:
        pass

    def caller(function, *args):
        function(*args)

    for _ in range(10000):
        caller(dummy, "hello world", 100)

def bm_direct_function_call():
    def dummy(name: str, age: int) -> None:
        pass

    for _ in range(10000):
        dummy("hello world", 100)

if __name__ == "__main__":
    run_bms = {
        "Buffer": [
            "bm_presize_bytearray_memoryview",
            "bm_presize_bytearray",
            "bm_bytearray_extend",
            "bm_bytearray_plus",
            "bm_bytearray_plus_reverse",
            "bm_BytesIO",
            "bm_ctypes_string_buffer",
        ],
        "Object": [
            "bm_TypedDict",
            "bm_class_vanilla_obj",
            "bm_vanilla_dict",
            "bm_pass_function_to_caller",
            "bm_direct_function_call",
        ]
    }

    # Sanity check
    for bm in run_bms["Buffer"]:
        assert len(globals()[bm]()) == 10000 * 11
    
    # CPU profiling
    print("\nCPU profiling:\n")
    import timeit
    for group, bms in run_bms.items():
        print(f"\n{group} benchmarks:")
        for bm in bms:
            time = timeit.timeit(f"{bm}()", globals=globals(), number=1000)
            space = " " * (len(max(bms, key=len)) - len(bm))
            print(f"{bm}: {space}{time}")

    # MEMORY profiling
    print("\nMemory profiling:\n")
    import tracemalloc
    for group, bms in run_bms.items():
        print(f"\n{group} benchmarks:")
        for bm in bms:
            tracemalloc.start()
            globals()[bm]()
            space = " " * (len(max(bms, key=len)) - len(bm))
            print(f"{bm}: {space}{tracemalloc.get_traced_memory()}")
            tracemalloc.stop()
