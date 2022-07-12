# Frog2
N, K = map(int, input().split())
h = list(map(int,input().split()))

dp = [2 ** 31 - 1] * N

dp[0] = 0

for i in range(1, N):
    for j in range(1, min(i, K) + 1):
        tmp = dp[i - j] + abs(h[i] - h[i - j])
        if tmp < dp[i]:
            dp[i] = tmp

print(dp[N - 1])
