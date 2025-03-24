from string import ascii_lowercase

essay = input('Submit your essay: ')

if not set(essay).issubset(ascii_lowercase + ' ,._'):
    print('Your essay contains invalid characters')
    exit()

if len(essay.split(' ')) > 100:
    print('Exceeded word limit!')
    exit()

if '__builtins__' in essay:
    exit()

score = eval(essay, {'__builtins__': {}}, {})

if score > 90:
    print('You scored: A')
elif score > 80:
    print('You scored: B')
elif score > 70:
    print('You scored: C')
elif score > 60:
    print('You scored: D')
elif score > 50:
    print('You scored: E')
elif score > 0:
    print('You scored: F')
elif score == 0:
    print('How did you even score that low?')
    print(open('flag.txt').read())

