print(0if input()=='0'else sorted(map(int,input().split()),key=lambda x:-x if x<0else x-.1)[0])