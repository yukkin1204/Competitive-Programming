# 2次元の累積和
from sys import stdin
H, W = map(int, input().split())
X = [list(map(int, stdin.readline().split())) for _ in range(H)]
Q = int(input())
l = [list(map(int, stdin.readline().split())) for _ in range(Q)]

csum = [[0] * (W + 1) for _ in range(H + 1)]

# 0行や0列は0のまま
for i in range(H):
    for j in range(W):
        csum[i + 1][j + 1] = csum[i + 1][j] + csum[i][j + 1] - csum[i][j] + X[i][j]

for tmp in l:
    A, B, C, D = tmp[0], tmp[1], tmp[2], tmp[3]
    print(csum[C][D] - csum[A - 1][D] - csum[C][B - 1] + csum[A - 1][B - 1])
