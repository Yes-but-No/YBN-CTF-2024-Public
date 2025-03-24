from Crypto.Util.number import getPrime, bytes_to_long
from math import gcd
from random import choice, randint
from secret import some_randbytes, flag
from hashlib import md5

def corrupt(flag):

    # since most of u didn't need it :p
    message = flag[6:-1]
    corrupted_index = []
    corrupted_message = []
    corrupts_list = some_randbytes
    # e.g. some_randbytes[0] = "01010101"

    for char, corrupts in zip(message, corrupts_list):
        in_bin = list(f'{char:08b}')
            
        for i in range(len(in_bin)):
            if corrupts[i] == '0':
                if in_bin[i] == '1':
                    in_bin[i] = '0'
                else:
                    in_bin[i] = '1'
            
        new_bin = ""
        for bit in in_bin:
            new_bin += bit

        corrupted_message += [new_bin]
        corrupted_index += [corrupts]

    return corrupted_index, corrupted_message

def gen_virus():
    viruses = []
    for _ in range(8):
        virus = 1
        for _ in range(20):
            virus *= randint(2**13, 2**14)
        viruses.append(virus)
    return viruses

def gen_private():
    a = []
    for i in range(8):
        a.append(getPrime(128))
    return a

def gen_public(a):
    while True:
        b = []
        n = getPrime(256)
        m = getPrime(256)

        for i in range(8):
            b.append((a[i] * n) % m)
        
        if all(gcd(i,j) == 1 or i == j for i in b for j in b):
            break
    return (n, m, b)

def encrypt(message, b):
    enc = []
    viruses = gen_virus()

    for in_bin in message:
        c = 1
        for i in range(len(in_bin)):
            if in_bin[i] == '1':
                if choice([0,1]) == 1:
                    c *= choice(viruses)
                c *= b[i]
        enc.append(c)
        
    return enc


def main():
    corrupted_index, corrupted_message = corrupt(flag)
    a = gen_private()
    _,m,b = gen_public(a)
    enc = encrypt(corrupted_index, b)
    print("m =", m)
    print("enc =", enc)
    print("corrupted_message =", corrupted_message)
    print("hash =", md5(flag).hexdigest())

main()