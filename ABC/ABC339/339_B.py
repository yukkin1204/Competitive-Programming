H, W, N = map(int, input().split())

l = [["."] * W for _ in range(H)]
x, y = 0, 0
d = 0

for i in range(N):
    if l[y][x] == ".":
        l[y][x] = "#"
        d = (d + 1) % 4
    else:
        l[y][x] = "."
        d = (d - 1) % 4
    if d == 0:
        y = (y - 1) % H
    elif d == 1:
        x = (x + 1) % W
    elif d == 2:
        y = (y + 1) % H
    else:
        x = (x - 1) % W

for row in l:
    print(*row, sep="")

