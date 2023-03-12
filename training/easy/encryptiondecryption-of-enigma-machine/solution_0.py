import sys
import math

def cae_shift(c, v):
    return chr((ord(c) - ord('A') + v)%26 + ord('A'))

def inc_shift(s, p):
    res = ''
    for i, c in enumerate(s):
        res += cae_shift(c, p+i)
    return res

def inv_inc_shift(s, p):
    res = ''
    for i, c in enumerate(s):
        res += cae_shift(c, -p-i)
    return res
# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

operation = input()
pseudo_random_number = int(input())
message = ''
if operation == 'ENCODE':
    dic1 = {a:b for a, b in zip(map(chr, range(ord('A'), ord('Z')+1)), input())}
    dic2 = {a:b for a, b in zip(map(chr, range(ord('A'), ord('Z')+1)), input())}
    dic3 = {a:b for a, b in zip(map(chr, range(ord('A'), ord('Z')+1)), input())}
    message = input()
    message = inc_shift(message, pseudo_random_number)
    message = ''.join(list(map(lambda c: dic3[dic2[dic1[c]]], message)))
else:
    inv_dic1 = {b:a for a, b in zip(map(chr, range(ord('A'), ord('Z')+1)), input())}
    inv_dic2 = {b:a for a, b in zip(map(chr, range(ord('A'), ord('Z')+1)), input())}
    inv_dic3 = {b:a for a, b in zip(map(chr, range(ord('A'), ord('Z')+1)), input())}
    message = input()
    message = ''.join(list(map(lambda c: inv_dic1[inv_dic2[inv_dic3[c]]], message)))
    message = inv_inc_shift(message, pseudo_random_number)
    
print(message)
