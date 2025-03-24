from random import choice, shuffle, randint
from tqdm import tqdm

K = 10000
questions = ["Yes, or No", "y/n", "no but actually yes", "是或者不是", 
             "ya atau tidak", "ஆம் அல்லது இல்லை", "iva jew le", "ja oder nein", 
             "oui ou non", "はい、もしくは、いいえ", "예 또는 아니오", "có hay không"]

answer = ["Yes", "No", "y", "n", "yes but actually no", "不", "是", 
          "tidak", "ya", "iva", "le", "ja", "nein", "non", "oui",
        "không", "có", "예", "아니오", "はい", "いいえ", "ஆம்", "இல்லை"]

orderr = list(range(K))
shuffle(orderr)


def gen_code(i):
    a, b = choice("*+-^"), randint(1, 2**64-1)
    return (f"""
void ybn{i}() {{
    char s[100];
    printf("{choice(questions)}?\\n");
    fgets(s, 100, stdin);
    if (!strcmp(s, "{choice(answer)}\\n")) {{
        x {a}= {b};
        return {"ybn" + str(orderr[orderr.index(i)-1]) + "();" if i != orderr[0] else "print_flag();"}
    }}
    exit({i});
}}
""", a, b)


file = open("yesbutno.cpp", "wb")
header = """
#include <stdio.h>
#include <string.h>
#include <iostream>

unsigned long long x = 0x7965736275746e6f;
void print_flag();
"""

items = []
x = 0x7965736275746e6f
file.write(header.encode())
for i in range(K):
    file.write(f"void ybn{i}();\n".encode())
for i in range(K):
    script, op, val = gen_code(i)
    file.write(script.encode())
    items.append((op, val))
for i in orderr[::-1]:
    op, val = items[i]
    if op == '+':
        x += val
    elif op == '-':
        x -= val
    elif op == '*':
        x *= val
    else:
        x ^= val
    x %= 2**64


flag = b"YBN24{y3s_bUt_No_w4!t_actU4lly_ye5_buTt_n0_mAYb3_yEs}"
while len(flag) % 8:
    flag += b'\x00'
ct = []
for i in range(0, len(flag), 8):
    y = int.from_bytes(flag[i:i+8], 'little')
    y *= pow(x, -1, 2**64)
    y %= 2**64
    ct.append(str(y))


footer = f"""
void print_flag(){{
    long long enc[{len(ct)}] = {{{", ".join(ct)}}};
    for (int i = 0; i < {len(ct)}; i++) {{
        long long y = enc[i];
        y *= x;
        while (y) {{
            printf("%c", y % 256);
            y /= 256;
        }}
    }} 
    printf("\\n");
}}

int main() {{
    ybn{orderr[-1]}();
    return 0;
}}
"""
file.write(footer.encode())
print("Done.")