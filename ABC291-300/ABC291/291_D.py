# D - Flip Cards
from sys import stdin
N = int(input())
l = [list(map(int, stdin.readline().split())) for _ in range(N)]

# dp[i][j]:i+1枚目までの表裏の選び方の数
# j=0のときi+1枚目は表とし、j=1のときi+1枚目は裏とする
dp = [[0] * 2 for _ in range(N)]
dp[0][0] = 1
dp[0][1] = 1

for i in range(1, N):
    if l[i][0] != l[i - 1][0]:
        dp[i][0] += dp[i - 1][0]
    if l[i][0] != l[i - 1][1]:
        dp[i][0] += dp[i - 1][1]
    if l[i][1] != l[i - 1][0]:
        dp[i][1] += dp[i - 1][0]
    if l[i][1] != l[i - 1][1]:
        dp[i][1] += dp[i - 1][1]
    dp[i][0] = dp[i][0] % 998244353
    dp[i][1] = dp[i][1] % 998244353

print((dp[N - 1][0] + dp[N - 1][1]) % 998244353)
