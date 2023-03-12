import re
t = input()

t = re.sub(r'[\s,\.]+(,|\.)', r'\1', t)
t = re.sub(r'(,|\.)\s*([^\s])', r'\1 \2', t)
t = re.sub(r'([a-zA-Z])(.*?)\.', lambda m:f'{m.group(1).upper()}{m.group(2).lower()}.', t)
t = re.sub(r'([a-zA-Z])([^.]*?)$',lambda m:f'{m.group(1).upper()}{m.group(2).lower()}',t)
print(t)