import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

bits = input()
orig = "abcdefghijklmnop"
a = sum([int(bits[orig.index(c)]) for c in "abcdefghijklmnop"])%2

b = sum([int(bits[orig.index(c)]) for c in "bdfhjlnp"])%2
c = sum([int(bits[orig.index(c)]) for c in "cdghklop"])%2
e = sum([int(bits[orig.index(c)]) for c in "efghmnop"])%2
i = sum([int(bits[orig.index(c)]) for c in "ijklmnop"])%2

if [a,b,c,e,i] == [0,0,0,0,0]:
    print(bits)
else:
    err_col = 0
    if b == 0:
        if c == 0:
            err_col = 0
        else:
            err_col = 2
    else:
        if c == 0:
            err_col = 1
        else:
            err_col = 3
    err_row = 0
    if e == 0:
        if i == 0:
            err_row = 0
        else:
            err_row = 2
    else:
        if i == 0:
            err_row = 1
        else:
            err_row = 3
    bits=list(bits)
    err = err_row*4+err_col
    if a==0:
        print('TWO ERRORS')
    else:
        bits[err] = '1' if bits[err]=='0' else '0'
        print(''.join(bits))