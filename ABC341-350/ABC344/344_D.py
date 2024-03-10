T = input()
N = int(input())

INF = 10 ** 9
dp = [[INF for _ in range(len(T) + 1)] for _ in range(N + 1)]
dp[0][0] = 0

for i in range(N):
    S = list(input().split())[1:]
    for j in range(len(T) + 1):
        # 袋i+1を利用しない場合
        if dp[i][j] < dp[i + 1][j]:
            dp[i + 1][j] = dp[i][j]
        # 袋i+1を利用する場合
        for s in S:
            if s == T[j:j + len(s)]:
                if dp[i][j] + 1 < dp[i + 1][j + len(s)]:
                    dp[i + 1][j + len(s)] = dp[i][j] + 1

if dp[N][len(T)] < INF:
    print(dp[N][len(T)])
else:
    print(-1)
