# C - Coverage
N, M = map(int, input().split())
l = []
for i in range(M):
    c = int(input())
    s = set(map(int, input().split()))
    l.append(s)

count = 0
# bit全探索
for i in range(2 ** M):
    s = set()
    for j in range(M):
        if (i >> j) & 1:
            s = s.union(l[j])
    if len(s) == N:
        count += 1

print(count)