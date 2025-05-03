import itertools

N, M = map(int, input().split())
C = list(map(int, input().split()))
l = [list(map(int, input().split())) for _ in range(M)]

d = {i: [] for i in range(1, N + 1)}
for i, row in enumerate(l):
    for num in row[1:]:
        d[num].append(i + 1)

min_price = float("inf")

for pattern in itertools.product(range(3), repeat=N):
    price = sum(C[i] * pattern[i] for i in range(N))
    count = {i: 0 for i in range(1, M + 1)}
    for i in range(N):
        for num in d[i + 1]:
            count[num] += pattern[i]
    if all(count[i] >= 2 for i in range(1, M + 1)):
        min_price = min(min_price, price)

print(min_price)
