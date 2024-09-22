# C - PC on the Table
from sys import stdin
H, W = map(int, input().split())
S = [list(stdin.readline()[:-1]) for _ in range(H)]

for row in S:
    for i in range(W - 1):
        if row[i] == "T" and row[i + 1] == "T":
            row[i] = "P"
            row[i + 1] = "C"
    print(*row, sep="")