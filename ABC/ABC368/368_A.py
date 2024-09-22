N, K = map(int, input().split())
A = list(map(int, input().split()))

B = A[N - K : N] + A[0 : N - K]
print(*B)