from pprint import pprint
n = int(input())
mat = []
for i in range(n):
    compound = input()
    mat += [compound]

ml = max(map(len, mat))
mat = [[mat[j][i:i+3] for i in range(0,ml,3)] for j in range(n)]
for i in range(n):
    for j in range(len(mat[0])):
        conn_count = 0
        u = mat[i][j]
        if u[:2] == 'CH':
            comp = 4-int(u[2])
            for x,y in [(1,0),(0,1),(-1,0),(0,-1)]:
                try:
                    v = mat[i+x][j+y]
                    if v[0]=='(':
                        conn_count += int(v[1])
                except:pass
            if comp != conn_count:
                print('INVALID')
                exit(0)

print('VALID')