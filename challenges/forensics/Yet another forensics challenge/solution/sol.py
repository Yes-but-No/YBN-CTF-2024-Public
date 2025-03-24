import struct, base64,lzma

unpacked = lzma.decompress(base64.b64decode(open("dist/formatted-code.py").read()[73:-3]))

a = eval(unpacked.splitlines()[3][2:])

bits = ""

b=[]
for c in a:
    d = []
    for e in c[1]:
        f = ""
        e = [e[g:g+4] for g in range(0,len(e),4)]
        for h in e:
            red, green, blue, k = struct.unpack("BBBc", h)

            if len(bits) > 500:
                continue

            bits += bin(red)[-2:]
            bits += bin(green)[-2:]
            bits += bin(blue)[-2:]


str_data = ""
for i in range(0, len(bits), 8):
    binc = bits[i:i + 8]
    num = int(binc, 2)
    str_data += chr(num)
print(str_data)