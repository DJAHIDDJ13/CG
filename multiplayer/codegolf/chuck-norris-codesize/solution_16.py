import re
print(*['000  '['1'in i::2]+'0'*len(i)for i in re.findall('(?:1+|0+)',''.join([f'{ord(i):07b}'for i in input()]))])