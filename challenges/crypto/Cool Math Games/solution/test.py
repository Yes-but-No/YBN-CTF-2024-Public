import random
from string import *
value = "Vd8WHqRa9Wm2fTfnNTH4o2E4sXA1VMb4"
for i in range(0, 32768):
    random.seed(i)
    if value == "".join(random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789") for _ in range(32)):
        print(i)
        break
    print(f"Seed {i} failed")
    
answer = ""
random.seed(i)
print("".join([random.choice(ascii_lowercase + ascii_uppercase + digits) for _ in range(32)]))
print("".join([random.choice(ascii_lowercase + ascii_uppercase + digits) for _ in range(32)]))