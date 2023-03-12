a,b,u,v=map(int,input().split())
a,b,A=a-u,b-v,abs
print(*[a+b for a,b in zip(["NS"[b>0]]*A(b)+[""]*(A(a)-A(b)),["WE"[a>0]]*A(a)+[""]*(A(b)-A(a)))],sep='\n')