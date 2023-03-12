def LevenshteinDistance(s, t):
    m,n = len(s), len(t)

    v0 = [i for i in range(n+1)]
    v1 = [0 for i in range(n+1)]

    for i in range(m):
        v1[0] = i + 1

        for j in range(n):
            deletionCost = v0[j + 1] + 1
            insertionCost = v1[j] + 1
            if s[i] == t[j]:
                substitutionCost = v0[j]
            else:
                substitutionCost = v0[j] + 1

            v1[j + 1] = min(deletionCost, insertionCost, substitutionCost)

        v0, v1 = v1, v0

    return v0[n]
s = input()
t = input()
print(LevenshteinDistance(s, t))