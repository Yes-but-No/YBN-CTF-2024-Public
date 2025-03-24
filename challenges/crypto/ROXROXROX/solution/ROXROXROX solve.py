def binary_to_bytes(binary_string):
    if len(binary_string) % 8 != 0:
        raise ValueError("The length of the binary string should be a multiple of 8")

    byte_array = bytearray()
    for i in range(0, len(binary_string), 8):
        byte = binary_string[i:i+8]
        byte_array.append(int(byte, 2))
    
    return bytes(byte_array)

def xor(binary):
    if len(binary) == 1:
        return str(int(binary) ^ 1)
    
    pivot = len(binary) // 2
    return xor(binary[pivot:]) + xor(binary[:pivot])

def decrypt_xor(binary_string):
    decrypted_binary = xor(binary_string)
    return binary_to_bytes(decrypted_binary)

binary_string = '0100000110110001111100111110000110110001111100111110000110110001111100111110000100000101001100111001000101110011001100011011000101010001001110010011001110110001001000011101001110110011100011011011110101100101'
decrypted_bytes = decrypt_xor(binary_string)
print(f"Decrypted Bytes: {decrypted_bytes}")
print(f"Decrypted String: {decrypted_bytes.decode('utf-8', errors='ignore')}")
