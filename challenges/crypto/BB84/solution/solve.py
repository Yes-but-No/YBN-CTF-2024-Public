from pwn import xor
import random

fake_flag = b"YBN24{???????????????????????????????????????????}"

def measure(alice_bases, alice_bits, bob_bases):
    measured = []
    for i, j, k in zip(alice_bits, alice_bases, bob_bases):
        if k == j:
            measured.append(i)
        else:
            measured.append(random.randint(0, 1))
    return measured

def shift_key(bob_bases, alice_bases, measured):
    shifted_key = []
    for i, j, k in zip(measured, alice_bases, bob_bases):
        if k == j:
            shifted_key.append(i)
    return shifted_key

def one_time_pad(key, message):
    return xor(key, message)


length = 50

alice_bases = ['+', 'x', '+', '+', '+', '+', 'x', 'x', 'x', 'x', '+', 'x', '+', 'x', 'x', 'x', 'x', '+', 'x', '+', 'x', 'x', '+', 'x', '+', '+', 'x', '+', 'x', 'x', '+', '+', '+', '+', 'x', 'x', 'x', '+', 'x', 'x', 'x', '+', '+', 'x', '+', '+', 'x', 'x', '+', '+']        
alice_bits = [0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0]
bob_bases = ['+', 'x', 'x', '+', 'x', '+', '+', 'x', '+', 'x', '+', 'x', 'x', '+', 'x', 'x', 'x', '+', 'x', '+', '+', 'x', 'x', 'x', '+', 'x', 'x', 'x', '+', '+', 'x', '+', 'x', '+', '+', '+', '+', 'x', 'x', '+', '+', '+', 'x', '+', 'x', '+', 'x', 'x', 'x', 'x']
encrypted =  b'\xa49(\x9cOW\x08\x87\xdf\x06\x06\x1c\xc9\x18\xebq\x00@\x9e\xc0k\x0f\xe6z\x88\x98\x15\x15\x9f\rI\x06\xc6\xb4\r\x04Z\xd6>\x99}]+\xb5\xc1G%\xe0g\x85'
random_bytes = b'\xfdzf\xafz,X\xf3\xeahsh\xa5F\xa9\x139t\xc1\xf0\x18P\xd4\x03\xf8'

measured = measure(alice_bases, alice_bits, bob_bases)

shifted_key = shift_key(bob_bases, alice_bases, measured)[:len(fake_flag)]

one_time_pad_key = one_time_pad(shifted_key, random_bytes)
flag = one_time_pad(one_time_pad_key, encrypted)

print(flag)