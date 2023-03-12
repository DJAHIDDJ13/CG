r = int(input())
l = int(input())

seq = [r]

for i in range(l-1):
    new_seq = []
    el = seq[0]
    el_count = 1
    for s in seq[1:]:
        if el == s:
            el_count += 1
        else:
            new_seq += [el_count, el]
            el = s
            el_count = 1
    new_seq += [el_count, el]

    seq = new_seq
print(' '.join(map(str,seq)))