import random
from secret import flag

MOD = 2**61 - 1 # oo nice, a prime number!
xor = lambda x,y:bytes([i^j for i,j in zip(x,y)])

class LCG:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.x = random.getrandbits(64) % MOD
    
    def next(self):
        self.x = (self.x * self.a + self.b) % MOD
        return self.x % 2**32


class Cipher:
    def __init__(self, a, b):
        self.lcg = LCG(a, b)

    def encrypt(self, msg):
        msg += b'\x00' * (4 - len(msg) % 4)
        ctxt = b''    
        for i in range(0, len(msg), 4):
            msg_block = msg[i:i+4]
            lcg_block = (self.lcg.next()).to_bytes(4,"big")
            ctxt += xor(lcg_block, msg_block)
        return ctxt
    
for i in range(2):
    cipher = Cipher(2**31, 2**37)
    print(cipher.encrypt(flag).hex())
# 8f677a298b845380f3295cc44c9816d707a4b7b286ccbd3fee59c529cb94ce790a632054cc800c9beadb92ef
# aae87535d3e7a24cb83742fdfc5ff44e91988bc0e743760dc221bacc088b581d5293de9f4abf21525b3a7079