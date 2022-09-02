# Left Right Operation
# DPを用いた別解
# dp[i][j]
# iはどの位置か、jは現在位置がL(0)かA(1)かR(2)か
N, L, R = map(int, input().split())
A = list(map(int, input().split()))

dp = [[0] * 3 for _ in range(N)]
dp[0] = [L, A[0], R]

for i in range(1, N):
    dp[i][0] = dp[i - 1][0] + L
    dp[i][1] = min(dp[i - 1][0] , dp[i - 1][1]) + A[i]
    dp[i][2] = min(dp[i - 1][1] , dp[i - 1][2]) + R

print(min(dp[N - 1]))
