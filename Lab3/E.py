def main():
    T = int(input())
    for i in range(T):
        parts = input().split()
        base = int(parts[0])
        exp = int(parts[1])
        mod = int(parts[2])
        
        if base == 1:
            print(exp % mod)
        else:
            numerator = (ModPow(base, exp + 1, mod * (base - 1)) - base) % (mod * (base - 1))
            inv = ModInverse(base - 1, mod)
            result = (numerator // (base - 1)) % mod  
            print(result)


def ModPow(base, exp, mod):
    if exp == 0:
        return 1
    if exp % 2 == 0:
        half = ModPow(base, exp // 2, mod)
        return (half * half) % mod
    else:
        return (base * ModPow(base, exp - 1, mod)) % mod


def ModInverse(base, mod):
    return ModPow(base, mod - 2, mod)

main()