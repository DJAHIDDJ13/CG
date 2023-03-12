height, width = [int(i) for i in input().split()]
nums = []
mask = []
for i in range(height):
    line = input()
    nums += map(int, line.split())
for i in range(height):
    line = input()
    mask += line.split()

seq = [a for a, b in zip(nums, mask) if b == 'X']
print(str(all(v < 0 for v in seq[::2]) and all(v > 0 for v in seq[1::2]) or all(v > 0 for v in seq[::2]) and all(v < 0 for v in seq[1::2])).lower())