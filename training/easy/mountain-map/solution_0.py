n = int(input())

heights = list(map(int, input().split()))
max_h = max(heights)
mountains = [""] * max_h
for height in heights:
    for i in range(max_h):
        if i >= max_h-height:
            j = i-(max_h-height)
            mountains[i] += " " *(height-1-j)+"/"+" " *2*j +"\\"+" " *(height-1-j)
        else:
            mountains[i] += " "*2*height

print("\n".join(map(str.rstrip, mountains)))
