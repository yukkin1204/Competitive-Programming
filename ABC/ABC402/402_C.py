N, M = map(int, input().split())
l = [list(map(int, input().split())) for _ in range(M)]
B = list(map(int, input().split()))

d = {i: [] for i in range(1, N + 1)}
K = []
ans = 0

for i, row in enumerate(l):
    K.append(row[0])
    for num in row[1:]:
        d[num].append(i + 1)

for num in B:
    if num in d:
        for i in d[num]:
            K[i - 1] -= 1
            if K[i - 1] == 0:
                ans += 1
    print(ans)
