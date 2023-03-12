def combineseq(X, Y):
    if X in Y:
        return Y, X
    elif Y in X:
        return X, Y
    
    subseq1, subseq2 = '', ''
    comb1, comb2 = '', ''
    n = min(len(X), len(Y))
    for i in range(n,0,-1):
        if X[-i:] == Y[:i]:
            subseq1 = X[-i:]
            comb1 = X[:-i] + subseq1 + Y[i:]
            break
    
    X, Y = Y, X
    for i in range(n,0,-1):
        if X[-i:] == Y[:i]:
            subseq2 = X[-i:]
            comb2 = X[:-i] + subseq2 + Y[i:]
            break
    
    if len(subseq1) > len(subseq2):
        return comb1, subseq1
    else:
        return comb2, subseq2

n = int(input())
subseqs = []
for i in range(n):
    subseq = input()
    subseqs += [subseq]

changed = True
while len(subseqs) > 1 and changed:
    changed = False
    contenders = []
    for i,s in enumerate(subseqs[1:]):
        v, subseq = combineseq(subseqs[0], s)
        if v:
            subseqs.pop(i+1)
            subseqs[0] = v
            changed = True
            break

print(len(''.join(subseqs)))
