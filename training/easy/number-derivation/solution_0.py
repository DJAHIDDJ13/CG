from math import prod

def is_prime(k):
    for i in range(2, int(k**.5)+1):
        if k % i == 0:
            return False
    return True

first_primes = [*filter(is_prime, range(2,10000))]
def factorize(v):
    f = []
    for p in first_primes:
        if v == 1:
            break
        
        while v % p == 0:
            f.append(p)
            v //= p
    return f

def derive_num(n):
    f = factorize(n)
    if len(f) == 1:
        return 1

    n, m = f[0], prod(f[1:])
    return derive_num(n) * m + n * derive_num(m)

n = int(input())
print(derive_num(n))