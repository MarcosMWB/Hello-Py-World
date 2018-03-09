def cryptography(s):
    c = list(s)
    for i in range(0, len(s)):
        if c[i] == 'a' and c[i + 1] == 's':
            c[i] = 'x'
            c[i + 1] = 'a'

        elif c[i] == 'a' and c[i + 1] == 'r':
            c[i] = 'y'
            c[i + 1] = 'a'
        elif c[i] == 'ã' and c[i + 1] == 'o':
            c[i] = 'x'
            c[i + 1] = 'y'
        elif c[i] == 'ã' and not c[i + 1] == 'o':
            c[i] = 'x'
            c[i + 1] = 'z'
        elif c[i] == 'A':
            c[i] = '&'
        elif c[i] == 'a' and not c[i-1] == 'y':
            c[i] = '*'
        elif c[i] == ' ':
            c[i] = '^'
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
                        c[i] = chr(ord(c[i])-1)
            else:
                for j in range(98, 120):
                    if ord(c[i]) == j:
                        c[i] = chr(ord(c[i])-1)
    s = ''.join([str(s) for s in c])
    return s


print(str(cryptography(input('Type here: '))))
