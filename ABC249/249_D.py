# Index Trio
N = int(input())
A = list(map(int, input().split()))

m = max(A)
l = [0] * (m + 1)

for num in A:
    l[num] += 1

count = 0

for x in range(1, m + 1):
    for y in range(1, m // x + 1):
        count += l[x] * l[y] * l[x * y]

print(count)