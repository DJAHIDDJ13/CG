import sys
import math

def is_cube(n):
    cube_root = round(n**(1./3.))
    return cube_root ** 3 == n

orb_size_min, orb_size_max = [int(i) for i in input().split()]
glowing_size_1, glowing_size_2 = [int(i) for i in input().split()]

sphere = lambda s,b:s**3+b**3

glowing_vol = glowing_size_1 ** 3 + glowing_size_2 ** 3
valid = True
for a in range(orb_size_min, orb_size_max+1):
    b = glowing_vol - a ** 3
    if b > 0 and is_cube(b) and orb_size_min**3 <= b <= orb_size_max**3:
        b = round(b**(1./3))
        a, b = (b, a) if b < a else (a, b)
        if (a, b) != (glowing_size_1, glowing_size_2):
            print(a,b)
            break
else:
    print('VALID')
