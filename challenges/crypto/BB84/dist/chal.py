# https://medium.com/quantum-untangled/quantum-key-distribution-and-bb84-protocol-6f03cc6263c5

from pwn import xor
import random

flag = b"YBN24{???????????????????????????????????????????}"

def random_bit_string(length):
    return [random.randint(0, 1) for _ in range(length)]

def random_bases(length):
    return [random.choice(['+', 'x']) for _ in range(length)]

def measure(alice_bases, alice_bits, bob_bases):
    # TODO
    pass

def shift_key(bob_bases, alice_bases, measured):
    # TODO
    pass

def one_time_pad(key, message):
    return xor(key, message)


length = 50

alice_bits = random_bit_string(length)
alice_bases = random_bases(length)

bob_bases = random_bases(length)
measured = measure(alice_bases, alice_bits, bob_bases)

shifted_key = shift_key(bob_bases, alice_bases, measured)[:len(flag)]

random_bytes = random.randbytes(len(shifted_key))
one_time_pad_key = one_time_pad(shifted_key, random_bytes)
encrypted = one_time_pad(one_time_pad_key, flag)

print("alice_bases =", alice_bases)
print("alice_bits =", alice_bits)
print("bob_bases =", bob_bases)
print("encrypted = ", encrypted)
print("random_bytes =", random_bytes)