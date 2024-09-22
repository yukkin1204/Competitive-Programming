N = int(input())
S = input()
C = list(map(int, input().split()))

# iを文字数、jを最後の文字が0か1、kを連続済みかのflgとし、dp[i][j][k]をその条件を満たす文字列のcostの最小値とする
INFTY = 2 ** 31 - 1
dp = [[[INFTY] * 2 for _ in range(2)] for _ in range(N + 1)]
dp[0][0][0] = 0
dp[0][1][0] = 0

for i in range(N):
    if S[i] == "0":
        dp[i + 1][0][0] = dp[i][1][0]
        dp[i + 1][1][0] = dp[i][0][0] + C[i]
        if i >= 1:
            dp[i + 1][0][1] = min(dp[i][1][1], dp[i][0][0])
            dp[i + 1][1][1] = min(dp[i][0][1], dp[i][1][0]) + C[i]
    else:
        dp[i + 1][0][0] = dp[i][1][0] + C[i]
        dp[i + 1][1][0] = dp[i][0][0]
        if i >= 1:
            dp[i + 1][0][1] = min(dp[i][1][1], dp[i][0][0]) + C[i]
            dp[i + 1][1][1] = min(dp[i][0][1], dp[i][1][0])

print(min(dp[N][0][1], dp[N][1][1]))