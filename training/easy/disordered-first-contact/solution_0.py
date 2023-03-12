import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
message = input()
l = len(message)
stride = math.floor((math.sqrt(1 + 8*l) - 1) / 2)
first = l-stride*(stride+1)//2
start = 1 if stride % 2 else 0
if n > 0:
    for _ in range(n):
        if stride % 2:
            new = message[:first]
            message = message[first:]
        else:
            new = message[-first:]
            message = message[:-first]

        for i in range(stride):
            if i % 2 == start:
                s = message[:stride-i]
                message = message[stride-i:]
            else:
                s = message[-stride+i:]
                message = message[:-stride+i]

            new = s+new
        message = new
else:
    for _ in range(-n):
        new = ""
        for i in range(stride):
            s = message[:i+1]
            message = message[i+1:]
            if i % 2:
                new = s+new
            else:
                new = new+s

        message = new + message if i%2 else message + new

print(message)