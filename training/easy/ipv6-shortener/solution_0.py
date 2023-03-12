import sys
import math
import re
# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

ip = input()
ip = re.sub(r"(?<![a-f0-9])0+([a-f1-9]+)", r"\1", ip)

zero_seqs = list(re.finditer(r"^(0+:)+|(:0+)+$|:(0+:)+", ip))
if len(zero_seqs)>0:
    longest = max(zero_seqs, key=lambda x:len(x.group()))
    if len(list(filter(None,longest.group().split(':')))) > 1:
        ip = ip[:longest.start()]+"::"+ip[longest.end():]

ip = re.sub(r"(?<![a-f1-9])0+(?![a-f1-9])", "0", ip)
print(ip)