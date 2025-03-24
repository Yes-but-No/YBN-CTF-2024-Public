MOD = 2**61 - 1
xor = lambda x,y:bytes([i^j for i,j in zip(x,y)])

c0 = bytes.fromhex("8f677a298b845380f3295cc44c9816d707a4b7b286ccbd3fee59c529cb94ce790a632054cc800c9beadb92ef")
c1 = bytes.fromhex("aae87535d3e7a24cb83742fdfc5ff44e91988bc0e743760dc221bacc088b581d5293de9f4abf21525b3a7079")

def recover_lcg_x(ct, flag_start):
    # let hi, li denote the higher and lower 32 bits of xi
    # thus x1 = 2**32 * h1 + l1
    # then we have (2**32 * h1 + l1) * 2**31 + 2**37 == 2**32 * h2 + l2 (MOD 2**61-1) 
    # this simplifies into 4 * h1 + l1 * 2**31 + 2**37 == 2**32 * h2 + l2 (MOD 2**61-1) 
    # removing 2**32 and higher, we get
    # 4 * h1 + (l1 % 2) * 2**31 == l2
    # We use this relation to derive h1, and from there derive x1, thus recovering the initial x value in the LCG

    l1 = int.from_bytes(xor(ct[:4],  flag_start[:4] ), "big")
    l2 = int.from_bytes(xor(ct[4:8], flag_start[4:8]), "big")
    if l1 % 2:
        l2 -= 2**31 
    h1 = l2 // 4
    x = h1 * 2**32 + l1
    return x


def decrypt_lcg(ct, x):
    # Given the starting value in the LCG, decrypts the ciphertext
    flag = b""
    for i in range(0, len(ct), 4):
        flag += xor(ct[i:i+4], (x % 2**32).to_bytes(4,'big'))
        x = (x * 2**31 + 2**37) % MOD
    flag = flag.rstrip(b'\x00')
    return flag

# Now, to solve this we first brute for the 7th and 8th flag characters
# This gives us our first 2 lower 32-bit values in the lcg enabling us to recover the initial state x as demonstrated above
possible_flags = set()
for i in range(0x20, 0x7e): # printable ascii range
    for j in range(0x20, 0x7e):

        # Recover value of x when the LCG was initialised
        x0 = recover_lcg_x(c0, b"YBN24{" + bytes([i,j]))
        x1 = recover_lcg_x(c1, b"YBN24{" + bytes([i,j]))

        # Decrypt encrypted flags using LCG
        f0 = decrypt_lcg(c0, x0)
        f1 = decrypt_lcg(c1, x1)
        
        if f0 == f1 and all(0x20 <= k <= 0x7e for k in f0):
            possible_flags.add(f0)

print(possible_flags) # {b'YBN24{b7_c4r3fu9_0f_y0ub_par4m_Ch0ic3s.n.}', b'YBN24{b3_c4r3fu1_0f_y0ur_par4m_ch0ic3s...}'}
# of which we determine the latter to be the flag via eyepower
# nonetheless, both of these flags are deemed valid