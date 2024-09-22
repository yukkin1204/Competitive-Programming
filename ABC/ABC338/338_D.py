## 作成途中
N, M = map(int, input().split())
X = list(map(int, input().split()))
l = [0] * N
sum = 0

for i in range(M - 1):
    x1 = min(X[i], X[i + 1])
    x2 = max(X[i], X[i + 1])
    if x2 - x1 < x1 + N - x2:
        sum += x2 - x1
        for i in range(x1, x2):
            l[i] += (x1 + N - x2) - (x2 - x1)
    elif x2 - x1 > x1 + N - x2:
        sum += x1 + N - x2
        for i in range(x2, x1 + N):
            i = i % N
            l[i] += (x2 - x1) - (x1 + N - x2)
    else:
        sum += x2 - x1

min_value = min(l.tolist())
print(sum + min_value)

from itertools import accumulate
N, M = map(int, input().split())
X = list(map(int, input().split()))
res = [0] * (N + 10)
for i in range(M - 1):
    u, v = X[i] - 1, X[i + 1] - 1
    # どっち方向に進んでもコストは不変なので時計回りとして考える
    if u > v:
        u, v = v, u
    p = v - u
    q = N - p
    # 0を経由しない方
    res[u] += q
    res[v] -= q
    # 0を経由する方
    res[0] += p
    res[v] += p
    res[u] -= p
acc = list(accumulate(res))
ans = min(acc[:N])
print(ans)