# Better Students Are Needed!
N, X, Y, Z = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

l = [[0] * 4 for _ in range(N)]
counts = [0, 0, 0]
ans = []

for i in range(N):
    l[i][0] = i + 1
    l[i][1] = A[i]
    l[i][2] = B[i]
    l[i][3] = A[i] + B[i]

l.sort(reverse = True, key = lambda x: x[0])
l.sort(reverse = True, key = lambda x: x[1])
for i in range(N):
    if counts[0] == X: break
    elif l[i][0] not in ans:
        ans.append(l[i][0])
        counts[0] += 1

l.sort(reverse = True, key = lambda x: x[0])
l.sort(reverse = True, key = lambda x: x[2])
for i in range(N):
    if counts[1] == Y: break
    elif l[i][0] not in ans:
        ans.append(l[i][0])
        counts[1] += 1

l.sort(reverse = True, key = lambda x: x[0])
l.sort(reverse = True, key = lambda x: x[3])
for i in range(N):
    if counts[2] == Z: break
    elif l[i][0] not in ans:
        ans.append(l[i][0])
        counts[2] += 1

ans.sort()
print(*ans, sep = "\n")
