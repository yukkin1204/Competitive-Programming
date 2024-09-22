H, W, N = map(int, input().split())
T = input()
S = [input() for _ in range(H)]

count = 0

for i in range(1, H - 1):
    for j in range(1, W - 1):
        if S[i][j] == "#":
            continue
        x, y = i, j
        flg = True
        for char in T:
            if char == "L":
                y -= 1
            if char == "R":
                y += 1
            if char == "U":
                x -= 1
            if char == "D":
                x += 1
            if S[x][y] == "#":
                flg = False
                break
        if flg:
            count += 1

print(count)