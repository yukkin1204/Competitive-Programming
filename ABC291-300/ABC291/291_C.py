# C - LRUD Instructions 2
N = int(input())
S = input()

x, y = 0, 0
# 通った座標をsetで管理
s = {(0, 0)}

for char in S:
    if char == "R":
        x += 1
    elif char == "L":
        x -= 1
    elif char == "U":
        y += 1
    else:
        y -= 1

    if (x, y) in s:
        print("Yes")
        exit()
    else:
        s.add((x, y))

print("No")