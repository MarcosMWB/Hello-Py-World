from __future__ import division


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


def check_next(i, s):
    if len(s) % (i + 1):
        return i + 1
    else:
        return -1


def cryptography(s, key_var):
    c = list(s)
    for i in range(0, len(s)):
        if c[i] == 'a' and c[check_next(i, s)] == 's':
            c[i] = 'x'
            c[i + 1] = 'a'

        elif c[i] == 'a' and c[check_next(i, s)] == 'r':
            c[i] = 'y'
            c[i + 1] = 'a'
        elif c[i] == 'ã' and c[check_next(i, s)] == 'o':
            c[i] = 'x'
            c[i + 1] = 'y'
        elif c[i] == 'ã' and not c[check_next(i, s)] == 'e':
            c[i] = 'x'
            c[i + 1] = 'z'
        elif c[i] == 'A':
            c[i] = '&'
        elif c[i] == 'a' and (c[i - 1] != 'y' and c[i - 1] != 'x'):
            c[i] = '*'
        elif c[i] == ' ':
            c[i] = '.'
        elif c[i] == ',':
            c[i] = ' '
        elif c[i] == '.':
            c[i] = ','
        elif c[i] == 'é':
            c[i] = 'í'
        elif c[i] == 'í':
            c[i] = 'ó'
        elif c[i] == 'ó':
            c[i] = 'ú'
        elif c[i] == 'ú':
            c[i] = 'é'

        else:
            if 65 < ord(c[i]) < 88:
                for j in range(66, 88):
                    if ord(c[i]) == j:
                        c[i] = chr(ord(c[i]) - key_var)
            else:
                for j in range(98, 120):
                    if ord(c[i]) == j:
                        c[i] = chr(ord(c[i]) - key_var)
    s = ''.join([str(s) for s in c])
    return s


print(str(cryptography(input('Text: '), create_key(input('Key: ')))))
