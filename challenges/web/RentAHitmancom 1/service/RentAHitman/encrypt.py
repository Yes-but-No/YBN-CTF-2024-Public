from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

def encrypt(KEY,SALT,iv,plaintext):
    padded = pad(plaintext.encode() + SALT.encode(), 16)
    cipher = AES.new(KEY, AES.MODE_CBC, iv=iv)
    try:
        encrypted = cipher.encrypt(padded)
    except ValueError as e:
        return {"error": str(e)}

    return {"ciphertext": (encrypted).hex()}

def decrypt(KEY,iv,encrypted):
    try:
        print(encrypted)
        encrypted = bytes.fromhex(encrypted)

        cipher = AES.new(KEY, AES.MODE_CBC, iv=iv)
        plaintext = cipher.decrypt(encrypted)

        # Unpad the plaintext and return it as a string
        plaintext = unpad(plaintext, 16).decode()
        return {"plaintext": plaintext}
    except ValueError as e:
        return {"error": str(e)}

