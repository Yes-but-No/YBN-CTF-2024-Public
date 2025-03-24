flag = b"YBN24{???????????????????}"

def bytes_to_binary(byte_string):
    return ''.join(format(byte, '08b') for byte in byte_string)

def xor(binary):
    if len(binary) == 1:
        return str(int(binary) ^ 1)
    
    pivot = len(binary) // 2
    return xor(binary[pivot:]) + xor(binary[:pivot])

print(xor(bytes_to_binary(flag)))