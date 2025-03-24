from sage.all import EllipticCurve, GF
from Crypto.Util.number import getPrime, getRandomInteger

KBITS = 512
p, q = getPrime(KBITS), getPrime(KBITS)
n = p*q
e = 65537
m = int.from_bytes(b"ybn24{?????????????????????????????????????????}", "big")
c = pow(m, e, n)

print(f'{n = }')
print(f'{e = }')
print(f'{c = }')

r = [getRandomInteger(8), getRandomInteger(8)]
print(f'{r = }')

Ep = EllipticCurve(GF(p), r)
Eq = EllipticCurve(GF(q), r)
En = Ep.order() * Eq.order()
print(f'{En = }')
