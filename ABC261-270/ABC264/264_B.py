# Nice Grid
# 愚直にやるなら基礎問題
R, C = map(int, input().split())
color = "white"

if (R == 1 or R == 15):
    color = "black"
elif (R == 2 or R == 14) and (C == 1 or C == 15):
    color = "black"
elif (R == 3 or R == 13) and (C == 1 or C == 15 or 3 <= C <= 13):
    color = "black"
elif (R == 4 or R == 12) and (C == 1 or C == 15 or C == 3 or C == 13):
    color = "black"
elif (R == 5 or R == 11) and (C == 1 or C == 15 or C == 3 or C == 13 or 5 <= C <= 11):
    color = "black"
elif (R == 6 or R == 10) and (C == 1 or C == 15 or C == 3 or C == 13 or C == 5 or C == 11):
    color = "black"
elif (R == 7 or R == 9) and (C == 1 or C == 15 or C == 3 or C == 13 or C == 5 or C == 11 or 7 <= C <= 9):
    color = "black"
elif R == 8 and (C == 1 or C == 15 or C == 3 or C == 13 or C == 5 or C == 11 or C == 7 or C == 9):
    color = "black"

print(color)