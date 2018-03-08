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


print(modular_exponential(int(input('Base: ')), int(input('Power: ')), int(input('Mod: '))))
