import sys
import math

def seek_position(player_pos, seek_pos):
    tx, ty = player_pos
    gx, gy = seek_pos
    mx, my = tx - gx, ty - gy
    command = ""

    if my > 0:
        command += "N"
        ty -= 1
    elif my < 0:
        command += "S"
        ty += 1
    if mx > 0:
        command += "W"
        tx -= 1
    elif mx < 0:
        command += "E"
        tx += 1
    return (tx, ty), command if command else "WAIT"

light_x, light_y, initial_tx, initial_ty = [int(i) for i in input().split()]
currentX = initial_tx
currentY = initial_ty
# game loop
while True:
    remaining_turns = int(input())  # The remaining amount of turns Thor can move. Do not remove this line.
    (new_pos, command) = seek_position((currentX, currentY), (light_x, light_y))
    currentX, currentY = new_pos
    print(command)