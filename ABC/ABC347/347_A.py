N, K = map(int, input().split())
A = list(map(int, input().split()))

l = []
for num in A:
    if num % K == 0:
        l.append(num // K)
print(*l)
