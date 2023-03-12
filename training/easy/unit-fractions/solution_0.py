from math import gcd, prod
from functools import lru_cache
import sys
from itertools import product

@lru_cache
def find_prime_factors(n):
    factors = []
    i = 2
    while i <= n:
        if n % i == 0:
            factors.append(i)
            n //= i
        else:
            i += 1
    return factors

def find_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    return sorted(divisors)

def prime_factor_combinations(prime_factors, n):
    allowed_factors = sorted([f for f in prime_factors if f <= n])
    combinations = set()
    for r in range(1, 7):#weird but meh
        for c in product(allowed_factors, repeat=r):
            c = prod(c)
            if c <= n:
                combinations.add(c)
    return combinations

n = int(input())
ys = set()

ys.update(find_divisors(n))
ys.update(prime_factor_combinations(find_prime_factors(n), n))
print(prime_factor_combinations(find_prime_factors(n), n), file=sys.stderr)

for y in sorted(ys):
    y += n
    x = -(n * y) // (n - y)
    if n*(x+y) == (x*y):
        print(f"1/{n} = 1/{x} + 1/{y}")