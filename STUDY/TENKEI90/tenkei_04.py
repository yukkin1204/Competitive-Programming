# Cross Sum
# 全探索。各行の和、各列の和を保存することがミソ
from sys import stdin

H, W = map(int, input().split())
A = [list(map(int, stdin.readline().split())) for _ in range(H)]

sum_H = [0] * H # 各行のsumを保存
sum_W = [0] * W # 各列のsumを保存

for i in range(H):
    for j in range(W):
        sum_H[i] += A[i][j]
        sum_W[j] += A[i][j]

for i in range(H):
    B = [0] * W
    for j in range(W):
        # 自分自身を2回足してしまうので1回分引く
        B[j] = sum_H[i] + sum_W[j] - A[i][j]
    print(*B)

