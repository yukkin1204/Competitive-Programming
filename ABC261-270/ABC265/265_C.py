# C - Belt Conveyor
H, W = map(int, input().split())
G = [list(input()) for _ in range(H)]

i, j = 1, 1
for _ in range(H * W + 1):
    if G[i - 1][j - 1] == "U":
        if i == 1:
            print(i, j)
            exit()
        else:
            i -= 1
    elif G[i - 1][j - 1] == "D":
        if i == H:
            print(i, j)
            exit()
        else:
            i += 1
    elif G[i - 1][j - 1] == "L":
        if j == 1:
            print(i, j)
            exit()
        else:
            j -= 1
    elif G[i - 1][j - 1] == "R":
        if j == W:
            print(i, j)
            exit()
        else:
            j += 1

print(-1)
