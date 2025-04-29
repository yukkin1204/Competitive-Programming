N, K = map(int, input().split())

if N < K:
    print(1)
    exit()

A = [0] * (N + 1)

for i in range(N + 1):
    if i < K:
        A[i] = 1
    elif i == K:
        A[i] = K
    else:
        A[i] = (A[i - 1] * 2 - A[i - K - 1]) % 1000000000

print(A[N])
