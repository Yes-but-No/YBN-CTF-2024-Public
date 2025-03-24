#Put a = 2, b as 1
#Other solutions possible, can choose a = 10, so can remove trailing 0s when convert to string

from Crypto.Util.number import inverse, long_to_bytes
from sympy import gcd
from pwn import remote

io = remote('34.50.70.45', 20595)
io.recvuntil(b'a: ')
io.sendline(b'2')
io.recvuntil(b'b: ')
io.sendline(b'1')

values = io.recv().decode().split('\n')[:-1]

g = int(values[0][4:])
n = int(values[1][4:])
ct = int(values[2][5:])

y = gcd(ct, n)
q = gcd(g, n)
enc = ct // y

# divide n by q and y, keep dividing by 2 until get prime which is p and solve
# p * 2**k = n // q // y

p2 = n // q // y
k = 0
while p2 % 2 == 0:
    p2 //= 2
    k += 1
p = p2
e = g // q

phi = (y-1) * (p-1) * (q-1) * (2**k - 2**(k-1))
d = inverse(e, phi)

flag = long_to_bytes(pow(enc, d, n))
print(flag)