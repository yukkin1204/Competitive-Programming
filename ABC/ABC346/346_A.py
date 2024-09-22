N = int(input())
A = list(map(int, input().split()))

l = []
for i in range(N - 1):
    l.append(A[i] * A[i + 1])
print(*l)