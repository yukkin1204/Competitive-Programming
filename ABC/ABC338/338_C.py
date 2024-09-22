N = int(input())
Q = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))

INF = 10 ** 18
ans = 0
x_max = INF

for i in range(N):
    if A[i] > 0:
        x_max = min(x_max, Q[i] // A[i])

for x in range(x_max + 1):
    Q2 = Q.copy()
    y = INF
    for i in range(N):
        if B[i] > 0:
            y = min(y, (Q2[i] - A[i] * x) // B[i])
    ans = max(ans, x + y)
print(ans)