from Crypto.Util.number import getPrime
from math import gcd

flag = b'YBN24{kn4p5@ck_Pr1m3s_GCD_At+4cK!!}'

def gen_private():
    a = []
    for i in range(8):
        a.append(getPrime(128))
    return sorted(a)

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

def encrypt(flag, b):
    enc = []
    in_bins = []

    for char in flag:
        in_bin = f'{char:08b}' 
        in_bins.append(in_bin)

        c = 1
        for i in range(len(in_bin)):
            if in_bin[i] == '1':
                c *= b[i]
        enc.append(c)
        
    return enc, in_bins

a = gen_private()
n,m,b = gen_public(a)
enc, in_bins = encrypt(flag, b)
print('n =',n)
print('m =',m)
print('enc =',enc)