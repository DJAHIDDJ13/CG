import re
print(*[['00 ','0 ']['1'in i]+'0'*len(i)for i in re.findall(r'(?:1+|0+)',''.join([f'{ord(i):07b}'for i in input()]))])