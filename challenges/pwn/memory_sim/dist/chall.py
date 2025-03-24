from string import printable

MLEN = 1000
READ_ONLY = 900
MEMORY = [0] * MLEN
MENU = """1. write
2. read
>> """

def write_string(s, ind):
    sl = len(s)
    if ind+sl >= len(MEMORY):
        return -1
    MEMORY[ind-1] = len(s)
    for i in range(ind, ind+sl):
        MEMORY[i] = ord(s[i-ind])
    return (ind-1) % MLEN


def read_string(ind):
    sl = MEMORY[ind]
    ind += 1
    if ind+sl >= len(MEMORY):
        return -1
    return "".join([chr(i) for i in MEMORY[ind:ind+sl]])


flag = "YBN24{?????????????????????????????????????}"
write_string(flag, 950)
cached = []
while True:

    choice = int(input(MENU))

    if choice == 1:
        ustr = str(input("Enter string\n>> "))
        if not all(i in printable for i in ustr):
            print("invalid string")
            continue
        uid = int(input("Enter address\n>> "))
        if uid >= READ_ONLY:
            print("sorry, this region's read only")
            continue
        res = write_string(ustr, uid)
        if res == -1:
            print("error")
            continue
        print("string written successfully! You can view it at", res)
        cached.append(res)

    elif choice == 2:
        uid = int(input("Enter address\n>> "))
        if uid not in cached:
            print("Hey, no out of bounds access! >:(")
            continue
        res = read_string(uid)
        if res == -1:
            print("error")
            continue
        print("Your string:", res)

    else:
        print("Invalid choice!")