import math
N, M = map(int, input().split())

INF = 10 ** 24
ans = INF

a_max = min(N, math.ceil(M ** (1 / 2)))
for a in range(1, a_max + 1):
    b = min(N, math.ceil(M / a))
    if a * b >= M and a * b < ans:
        ans = a * b

if ans < INF:
    print(ans)
else:
    print(-1)