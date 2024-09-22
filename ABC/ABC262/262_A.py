# World Cup
# 基礎問題
Y = int(input())
r = Y % 4

if r == 0:
    print(Y + 2)
elif r == 1:
    print(Y + 1)
elif r == 2:
    print(Y)
else:
    print(Y + 3)
