import sys
import numpy as np

n = int(input())
for i in range(n):
    inputs = input().split()
    name = ''.join(inputs[::3])
    a_name, b_name, c_name = [*name]
    a = np.array([int(inputs[1]), int(inputs[2])])
    b = np.array([int(inputs[4]), int(inputs[5])])
    c = np.array([int(inputs[7]), int(inputs[8])])
    
    ab_l = np.linalg.norm(b - a)
    bc_l = np.linalg.norm(c - b)
    ac_l = np.linalg.norm(c - a)
    side_nature = ""
    if ab_l != bc_l and bc_l != ac_l and ab_l != ac_l:
        side_nature = 'a scalene'
    elif ab_l == bc_l:
        side_nature = f"an isosceles in {b_name}"
    elif ab_l == ac_l:
        side_nature = f"an isosceles in {a_name}"
    elif bc_l == ac_l:
        side_nature = f"an isosceles in {c_name}"
    
    angles = {c_name: np.degrees(np.arccos((bc_l**2 + ac_l**2 - ab_l**2) / (2 * bc_l * ac_l))),
              a_name: np.degrees(np.arccos((ac_l**2 + ab_l**2 - bc_l**2) / (2 * ac_l * ab_l))),
              b_name: np.degrees(np.arccos((ab_l**2 + bc_l**2 - ac_l**2) / (2 * ab_l * bc_l)))}

    right_angles = [k for k, v in angles.items() if abs(v-90) < .000001]
    obtuse_angles = [k for k, v in angles.items() if v > 90]
    if len(right_angles) > 0:
        angle_nature = f"a right in {right_angles[0]}"
    elif len(obtuse_angles) > 0:
        most_obtuse = max(obtuse_angles, key=lambda x:angles[x])
        angle_nature = f"an obtuse in {most_obtuse} ({round(angles[most_obtuse])}°)"
    else:
        angle_nature =  'an acute'
    print(f"{name} is {side_nature} and {angle_nature} triangle.")