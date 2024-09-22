N = int(input())
A = []
for i in range(N):
    A.append(list(map(int, input().split())))

l = 1
for r in range(1, N + 1):
    l = A[max(l - 1, r - 1)][min(l - 1, r - 1)]

print(l)
