a,b,u,v=map(int,input().split())
for a,b in zip(abs(b:=b-v)*["NS"[b>0]]+(X:=[""]*99),abs(a:=a-u)*["WE"[a>0]]+X):print(a+b)