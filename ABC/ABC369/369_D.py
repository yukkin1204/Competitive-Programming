N = int(input())
A = list(map(int, input().split()))

INFTY = 2 ** 31 - 1
dp = [[-INFTY] * 2 for _ in range(N + 1)]
dp[0][0] = 0

for i in range(N):
    dp[i + 1][0] = max(dp[i][0], dp[i][1] + (A[i] * 2))
    dp[i + 1][1] = max(dp[i][0] + A[i], dp[i][1])

print(max(dp[N][0], dp[N][1]))