from __future__ import division


def check_next(i, s):
    if len(s) % (i + 1):
        return i + 1
    else:
        return -1


def modular_exponential(base, power, mod):
    if power < 0:
        return -1
    base %= mod
    result = 1

    while power > 0:
        if power & 1:
            result = (result * base) % mod
        power = power >> 1
        base = (base * base) % mod
    return result


def create_key(key):
    p = 1
    for n in range(0, len(key)):
        p = p * ord(key[n]) + 7
    return modular_exponential(7, p, 13)


def decryptography(s, key_var):
    c = list(s)
    i = 0
    if key_var == 0:
        key_var = 19
    while i < len(s):
        if c[i] == 'x' and c[check_next(i, s)] == 'a':
            c[i] = 'a'
            c[i + 1] = 's'
            i += 1
        elif c[i] == 'y' and c[check_next(i, s)] == 'a':
            c[i] = 'a'
            c[i + 1] = 'r'
            i += 1
        elif c[i] == 'x' and c[check_next(i, s)] == 'y':
            c[i] = 'ã'
            c[i + 1] = 'o'
            i += 1
        elif c[i] == 'x' and c[check_next(i, s)] == 'z':
            c[i] = 'ã'
            c[i + 1] = 'e'
            i += 1
        elif c[i] == '&':
            c[i] = 'A'
        elif c[i] == '*':
            c[i] = 'a'
        elif c[i] == '.':
            c[i] = ' '
        elif c[i] == ' ':
            c[i] = ','
        elif c[i] == ',':
            c[i] = '.'
        elif c[i] == 'í':
            c[i] = 'é'
        elif c[i] == 'ó':
            c[i] = 'í'
        elif c[i] == 'ú':
            c[i] = 'ó'
        elif c[i] == 'é':
            c[i] = 'ú'

        else:
            c[i] = chr(ord(c[i]) + key_var)
        i += 1
    s = ''.join([str(s) for s in c])
    return s


k = create_key(input('Key: '))
print(str(decryptography(input('Type here: '), k)))
