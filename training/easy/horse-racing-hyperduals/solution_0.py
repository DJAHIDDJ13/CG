import sys
def hyperdual(n, horses):
    def closest_pair_recursive(horses, low, high):
        if high - low <= 1:
            return sys.maxsize
        mid = (low + high) // 2
        left_min = closest_pair_recursive(horses, low, mid)
        right_min = closest_pair_recursive(horses, mid, high)
        min_distance = min(left_min, right_min)
        mid_x = horses[mid][0]
        strip = [horse for horse in horses if abs(horse[0] - mid_x) < min_distance]
        strip.sort(key=lambda x: x[1])
        for i, horse1 in enumerate(strip):
            for horse2 in strip[i + 1: i + 7]:
                if horse2[1] - horse1[1] >= min_distance:
                    break
                min_distance = min(min_distance, abs(horse1[0] - horse2[0]) + abs(horse1[1] - horse2[1]))
        return min_distance

    horses.sort(key=lambda x: x[0])
    return closest_pair_recursive(horses, 0, n)

n = int(input())
h = [list(map(int,input().split())) for _ in range(n)]

print(hyperdual(n, h))
