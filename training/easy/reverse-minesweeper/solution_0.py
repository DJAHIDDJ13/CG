from scipy.signal import convolve2d
import numpy as np

w = int(input())
h = int(input())

grid = np.array([[0 if c == '.' else 1 for c in input()] for _ in range(h)])
kernel = np.array([[1, 1, 1], 
                   [1, 1, 1], 
                   [1, 1, 1]])

filled = convolve2d(grid, kernel, mode="same")
filled = filled.astype("str")

filled[filled == '0'] = '.'
filled[grid == 1] = '.'

for line in filled:
    print(*line, sep="")