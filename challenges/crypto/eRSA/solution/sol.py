from sage.all import Zmod, EllipticCurve, factor, gcd

exec(open('output.txt','r').read())
# po = 8699266164073358900984252805212729760092216807897414394297507312225768108112775428520117595733779352303487701703240214617984344378920494463437916788712967
# qo = 7042889134829427759007724531884498488513636080784442924635506551507426116950123164982778078434568501733437221254092476947181397394785557879438635051801380

G = EllipticCurve(Zmod(n), [59, 28])(7, 28)
primes = [i[0] for i in list(factor(En, limit=2**20))[:-1]]
for prime in primes:
    try:
        _ = (En//prime) * G
    except ZeroDivisionError as err:
        pmul = int(str(err).split(" ")[2])
        p = gcd(pmul, n)
        if p != n:
            break

q = n // p
d = pow(e, -1, (p-1)*(q-1))
print(int(pow(c,d,n)).to_bytes(64, "big").lstrip(b'\x00'))