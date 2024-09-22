N = int(input())
A = list(map(int, input().split()))

d = dict()
for i in range(N):
    d[A[i]] = i + 1

l = []
tmp = -1
for i in range(N):
    l.append(d[tmp])
    tmp = d[tmp]

print(*l)