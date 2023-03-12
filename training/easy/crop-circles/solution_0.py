instructions = input().split()
crop = [[True] * 19 for _ in range(25)]
for y in range(25):
    for x in range(19):
        for i in instructions:
            if i.startswith("PLANTMOW"):
                i = i[8:]
                cell_value = not crop[y][x]
            elif i.startswith("PLANT"):
                i = i[5:]
                cell_value = True
            else:
                cell_value = False
            
            u, v, d= i[0], i[1], i[2:]
            u, v = ord(u)-ord('a'), ord(v)-ord('a')
            if (u - x) ** 2 + (v - y) ** 2 <= (int(d) / 2) ** 2:
                crop[y][x] =  cell_value
                
for y in range(25):
    for x in range(19):
        print(end="{}" if crop[y][x] else "  ")
    print()