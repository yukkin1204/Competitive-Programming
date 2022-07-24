# Frog1
# DPのポイントは、DP配列による値の再利用と漸化式
N = int(input())
h = list(map(int,input().split()))

# DP 配列を用意
# dp[i] には i 番目の足場にたどり着くために必要な最低コストを入れる
dp = [0] * N

# 初期条件を入力
dp[0] = 0
dp[1] = abs(h[1] - h[0])

# i-2, i-1, i の漸化式を作成
for i in range(2, N):
    dp[i] = min(dp[i - 2] + abs(h[i] - h[i - 2]), dp[i - 1] + abs(h[i] - h[i - 1]))

# dp 配列の末尾が N 番目の足場にたどり着くために必要なコストとなる
print(dp[N - 1])
