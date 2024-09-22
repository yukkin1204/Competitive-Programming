N, Q = map(int, input().split())
T = list(map(int, input().split()))

l = [1] * N
for num in T:
    l[num - 1] = (l[num - 1] + 1) % 2
print(sum(l))
