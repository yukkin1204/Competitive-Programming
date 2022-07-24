# Knapsack 2
from sys import stdin
N, W = map(int, input().split())
l = [list(map(int, stdin.readline().split())) for _ in range(N)]

INFTY = 2 ** 31 - 1
# DP_04と同様の解き方では、W<=10^9のため、TLE
# DP_04の双対を考えることで上手くいく
# i番目までの品物を価値がjであるように選んだときの重さの最小値をdp[i][j]とする動的計画法
# jは10^2*10^3=10^5まで考えればよい
dp = [[INFTY] * 100001 for _ in range(N + 1)]
dp[0][0]=0

for i in range(N):
    for j in range(100001):
        if j - l[i][1] >= 0 and dp[i][j - l[i][1]] + l[i][0] < dp[i][j]:
            dp[i + 1][j] = dp[i][j - l[i][1]] + l[i][0]
        else:
            dp[i + 1][j] = dp[i][j]

# dp[N][j]をjが大きいところから見ていって、初めてW以下になったときのjが答え
ans = 100000
while dp[N][ans] > W:
    ans -= 1
print(ans)
