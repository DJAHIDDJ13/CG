import re
t = input()
# remove spaces before punctuation
t = re.sub(r'[\s,\.]+(,|\.)', r'\1', t)
# one space after punctuation
t = re.sub(r'(,|\.)\s*([^\s])', r'\1 \2', t)
# All phrases ending in . are capitalized
t = re.sub(r'([a-zA-Z])(.*?)\.', lambda m:f'{m.group(1).upper()}{m.group(2).lower()}.', t)
# All phrases at the end of the line and not ending with . are capitalized
t = re.sub(r'([a-zA-Z])([^.]*?)$', lambda m:f'{m.group(1).upper()}{m.group(2).lower()}',t)
print(t)