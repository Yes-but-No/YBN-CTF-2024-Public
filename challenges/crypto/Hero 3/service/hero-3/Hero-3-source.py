from Crypto.Util.number import getPrime, bytes_to_long
import random

flag = b"YBN24{r0und1ng_up_w1th_f3rm4t's_l1ttl3_th30r3m}"

try:
    p1 = getPrime(64) 
    p2 = getPrime(512)
    e = getPrime(32)

    c = str(random.randint(0,999999999))
    a = input("a: ")
    b = input("b: ")

    check = ' 01qwertyuiopasdfghjklzxcvbnm%^&*()+-/><'

    for char in a:
        assert char not in check and char.isascii()
    
    for char in b:
        assert char not in check and char.isascii()

    a = eval(a + c)
    b = eval(b)
    d = int(a ** b)
    z = pow(p1, p2-d, p2)

    ct = pow(bytes_to_long(flag)*z, e, p2)

    print("e =", e)
    print("p2 =", p2)
    print("ct =", ct)

except:
    quit()

