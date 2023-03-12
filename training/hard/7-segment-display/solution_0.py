import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
c = input()
s = int(input())

digits = ['1110111', '0010001', '0111110', '0111011', '1011001', '1101011', '1101111', '0110001', '1111111', '1111011']
up = [" ".join([' '+[' ',c][digits[int(i)][1]=='1']*s+' ' for i in str(n)])]
upmid = [" ".join([[' ',c][digits[int(i)][0]=='1']+' ' * s+[' ',c][digits[int(i)][2]=='1'] for i in str(n)]) for _ in range(s)]
mid = [" ".join([' '+[' ',c][digits[int(i)][3]=='1']*s+' ' for i in str(n)])]
middown = [" ".join([[' ',c][digits[int(i)][4]=='1']+' ' * s+[' ',c][digits[int(i)][6]=='1'] for i in str(n)]) for _ in range(s)]
down = [" ".join([' '+[' ',c][digits[int(i)][5]=='1']*s+' ' for i in str(n)])]
total = up + upmid + mid + middown + down
print('\n'.join(map(str.rstrip, total)))