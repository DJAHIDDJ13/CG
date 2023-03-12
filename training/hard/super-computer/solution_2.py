n = int(input())
activities = [tuple(map(int, input().split())) for _ in range(n)]
activities.sort(key=lambda x: x[0]+x[1])
end = 0
count = 0
for i in range(n):
    if activities[i][0] >= end:
        end = activities[i][0] + activities[i][1]
        count += 1
print(count)