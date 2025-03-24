from Crypto.Util.number import getPrime, bytes_to_long

flag = b"YBN24{RS4_mu1t!prim3_f4ct0r1ng_bu7_m0r3_:D}"

p = getPrime(256)
q = getPrime(256)
y = getPrime(256)
e = getPrime(64)
c = getPrime(12)


try:
    a = int(eval(input("a: ")))
    b = int(eval(input("b: ")))
    
    assert a > 1
    assert b > 0 and b < c
    
except:
    quit()


g = q * e
n = ((a) ** (b + c)) * p * q * y

enc = pow(bytes_to_long(flag), e, n)

ct = enc * y

print("g = {}".format(g))
print("n = {}".format(n))
print("ct = {}".format(ct))


