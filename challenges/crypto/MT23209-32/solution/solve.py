from pwn import *
from mtcrack import MT23209Predictor

predictor = MT23209Predictor()
p = remote("127.0.0.1", 10080)

p.clean()


for i in range(726):
    p.sendline(b"123")
    line = p.recvuntil("The number I was thinking of was: ")
    correctans = int(p.recvline())
    p.clean()
    predictor.setrandbits(correctans, 32)

    # print(correctans, ", ", end="")
    if i % 20 == 0:
        print(i)

print("726 passed. State secured.")
# print("Next one will be", predictor.getrandbits(32))
# p.interactive()

for i in range(100):
    p.clean()
    predicted = str(predictor.getrandbits(32)).encode()
    p.sendline(predicted)
p.interactive()


