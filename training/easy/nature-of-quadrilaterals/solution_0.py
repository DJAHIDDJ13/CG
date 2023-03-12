import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
def dist(xa,xb,ya,yb):
    return (xb-xa)**2+(yb-ya)**2
n = int(input())
for i in range(n):
    a, x_a, y_a, b, x_b, y_b, c, x_c, y_c, d, x_d, y_d = input().split()
    x_a = int(x_a)
    y_a = int(y_a)
    x_b = int(x_b)
    y_b = int(y_b)
    x_c = int(x_c)
    y_c = int(y_c)
    x_d = int(x_d)
    y_d = int(y_d)
    
    side1 = dist(x_a,x_b,y_a,y_b)
    side2 = dist(x_b,x_c,y_b,y_c)
    side3 = dist(x_c,x_d,y_c,y_d)
    side4 = dist(x_d,x_a,y_d,y_a)
    rhom =  side1 == side2 == side3 == side4
    
    rect1 = dist(x_a,x_b,y_a,y_b)+dist(x_b,x_c,y_b,y_c) == dist(x_a,x_c,y_a,y_c)
    rect2 = dist(x_a,x_d,y_a,y_d)+dist(x_d,x_c,y_d,y_c) == dist(x_a,x_c,y_a,y_c)
    rect = rect1 and rect2
    
    para1 = (x_b-x_a) == (x_c-x_d)
    para2 = (y_b-y_a) == (y_c-y_d)
    para = para1 and para2
    if rect and rhom and para:
        print(a+b+c+d,"is a square.")
    elif para and not rect:
        if rhom:
            print(a+b+c+d,"is a rhombus.")
        else:
            print(a+b+c+d,"is a parallelogram.")
    elif rect:
        print(a+b+c+d,"is a rectangle.")
    else:
        print(a+b+c+d,"is a quadrilateral.")

