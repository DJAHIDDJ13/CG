import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
packet = input()
data = ""

while packet != '':
    p_ins = packet[:3]
    p_len = packet[3:7]
    p_id = packet[7:int(p_len,2)+7]
    data += f"001{p_len}{p_id}" if p_ins=='101' else ""
    packet = packet[int(p_len,2)+7:]
print(data)