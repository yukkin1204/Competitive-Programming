N, M = map(int, input().split())
l = [list(map(int, input().split())) for _ in range(M)]

d = {i: 0 for i in range(N)}
count = 0

for A, B in l:
    d[(A + B) % N] += 1

for key in d:
    count += d[key] * (d[key] - 1) // 2

print(M * (M - 1) // 2 - count)
