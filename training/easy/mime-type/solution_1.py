import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())  # Number of elements which make up the association table.
q = int(input())  # Number Q of file names to be analyzed.
mimeDict = {}
for i in range(n):
    # ext: file extension
    # mt: MIME type.
    ext, mt = input().split()
    mimeDict.update({ext.lower():mt})
print(mimeDict, file=sys.stderr)
for i in range(q):
    fname = input()  # One file name per line.
    print(fname, file=sys.stderr)
    if '.' in fname:
        ex = fname[len(fname) - fname[::-1].index('.'):]
        if ex.lower() in mimeDict:
            print(mimeDict[ex.lower()])
        else:
            print("UNKNOWN")
    else:
        print("UNKNOWN")
    
