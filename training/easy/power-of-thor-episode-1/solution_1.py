import sys
import math


light_x, light_y, initial_tx, initial_ty = [int(i) for i in input().split()]
currentX = initial_tx
currentY = initial_ty
# game loop
while True:
    remaining_turns = int(input())  # The remaining amount of turns Thor can move. Do not remove this line.
    moveX = currentX - light_x
    moveY = currentY - light_y
    
    if moveX != 0 and moveY !=0:
        if moveX > 0 and moveY > 0:
            print("NW")
            currentY -= 1
            currentX -= 1
        if moveX < 0 and moveY > 0:
            print("NE")
            currentX += 1
            currentY -= 1
        if moveX < 0 and moveY < 0:
            print("SE")
            currentX += 1
            currentY += 1
        if moveX > 0 and moveY<0:
            print("SW")
            currentX -= 1
            currentY += 1
    else:
        if moveX == 0:
            if moveY<0:
                print("S")
                currentY += 1
            if moveY>0:
                print("N")
                currentY -= 1
        if moveY == 0:
            if moveX > 0:
                print("W")
                currentX -= 1
            if moveX < 0:
                print("E")
                currentX += 1
