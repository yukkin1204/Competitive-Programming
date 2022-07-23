# Flipping and Bonus
# i回目でカウンタの数値がjであるときの金額の最大値をdp[i][j]とする動的計画法
# j≠0のとき、dp[i][j]に遷移するのはdp[i-1][j-1]からのみ
# j=0のとき、dp[i][j]=max(dp[i-1])
N, M = map(int, input().split())
X = list(map(int, input().split()))
d = dict()
for _ in range(M):
    C, Y = map(int, input().split())
    d[C] = Y

dp = [[0] * (N + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(i + 1):
        if j == 0:
            dp[i][j] = max(dp[i - 1])
        else:
            dp[i][j] += dp[i - 1][j - 1] + X[i - 1]
            if j in d:
                dp[i][j] += d[j]

print(max(dp[N]))