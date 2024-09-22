# 2次元の累積和
from sys import stdin
N = int(input())
XY = [list(map(int, stdin.readline().split())) for _ in range(N)]
Q = int(input())
l = [list(map(int, stdin.readline().split())) for _ in range(Q)]

A = [[0] * 1501 for _ in range(1501)]
csum = [[0] * 1501 for _ in range(1501)]

for pair in XY:
    A[pair[0]][pair[1]] += 1

for i in range(1500):
    for j in range(1500):
        csum[i + 1][j + 1] = csum[i + 1][j] + csum[i][j + 1] - csum[i][j] + A[i + 1][j + 1]

for tmp in l:
    a, b, c, d = tmp[0], tmp[1], tmp[2], tmp[3]
    print(csum[c][d] - csum[a - 1][d] - csum[c][b - 1] + csum[a - 1][b - 1])
