def encrypt(s):
    k1 = "kwR@r>Al"
    k2 = "F}T/X|m7"
    k3 = "pakU9BOT"
    k4 = "gj5'L}>?"

    key = k1 * 3 + (k3 + k1 + k2) * 2 + (k4 + k2) * 3 + k4 * 1

    return "".join([chr(ord(c) ^ ord(k)) for c, k in zip(s, key)])
