# Knapsack 1
from sys import stdin
N, W = map(int, input().split())
l = [list(map(int, stdin.readline().split())) for _ in range(N)]

# i番目までの品物を重さがj以下であるように選んだときの価値の最大値をdp[i][j]とする動的計画法
dp = [[0] * (W + 1) for _ in range(N + 1)]

for i in range(N):
    for j in range(W + 1):
        if j - l[i][0] >= 0 and dp[i][j - l[i][0]] + l[i][1] > dp[i][j]:
            dp[i + 1][j] = dp[i][j - l[i][0]] + l[i][1]
        else:
            dp[i + 1][j] = dp[i][j]

print(dp[N][W])
