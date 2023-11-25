N, L = map(int, input().split())
A = list(map(int, input().split()))

count = 0

for num in A:
    if num >= L:
        count += 1

print(count)
