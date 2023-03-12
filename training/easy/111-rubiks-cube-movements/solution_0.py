import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

rotations = input().split()
face_1 = input()
face_2 = input()
orig = "FBUDLR"
d = {"x'":"DUFBLR", "x":"UDBFLR",
     "y'":"RLUDFB", "y":"LRUDBF",
     "z'":"FBLRDU", "z":"FBRLUD"}
for r in rotations:
    face_1 = d[r][orig.index(face_1)]
    face_2 = d[r][orig.index(face_2)]
print(face_1)
print(face_2)