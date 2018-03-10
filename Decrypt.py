from __future__ import division


def check_next(i, s):
    if len(s) % (i + 1):
        return i + 1
    else:
        return -1


def decryptography(s):
    c = list(s)
    memory = 0
    for i in range(0, len(s)):
        if c[i] == 's' and memory == 1:
            c[i] = 's'
            memory = 0
        elif c[i] == 'r' and memory == 1:
            c[i] = 'r'
            memory = 0
        elif c[i] == 'o' and memory == 1:
            c[i] = 'o'
            memory = 0
        elif c[i] == 'e' and memory == 1:
            c[i] = 'e'
            memory = 0
        elif c[i] == 'x' and c[check_next(i, s)] == 'a':
            c[i] = 'a'
            c[i + 1] = 's'
            memory = 1
        elif c[i] == 'y' and c[check_next(i, s)] == 'a':
            c[i] = 'a'
            c[i + 1] = 'r'
            memory = 1
        elif c[i] == 'x' and c[check_next(i, s)] == 'y':
            c[i] = 'ã'
            c[i + 1] = 'o'
            memory = 1
        elif c[i] == 'x' and c[check_next(i, s)] == 'z':
            c[i] = 'ã'
            c[i + 1] = 'e'
            memory = 1
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
            c[i] = chr(ord(c[i])+1)
    s = ''.join([str(s) for s in c])
    return s


print(str(decryptography(input('Type here: '))))
