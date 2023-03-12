b=''.join(['{:07b}'.format(ord(i)) for i in input()])
r=['']
p=b[0]
for i in b:
 if i==p:r[-1]+=i
 else:r.append(i)
 p=i
print(' '.join([('0 'if i[0]=='1'else '00 ')+'0'*len(i) for i in r]))
