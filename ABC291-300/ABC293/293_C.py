# C - Make Takahashi Happy
from sys import stdin
H, W = map(int, input().split())
A = [list(map(int, stdin.readline().split())) for _ in range(H)]

count = 0

for i in range(2 ** (H + W - 2)):
    y, x = 0, 0
    S = {A[y][x]}

    for j in range(H + W - 2):
        if (i >> j) & 1:
            y += 1
            if y == H:
                break
        else:
            x += 1
            if x == W:
                break
        S.add(A[y][x])

    if len(S) == H + W - 1:
        count += 1

print(count)
