I=input
print(int(I()!='0')and min(map(int,I().split()),key=lambda x:[abs(x),x<0]))