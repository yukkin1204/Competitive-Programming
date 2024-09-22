N = int(input())
A = list(map(int, input().split()))

sum = 0
for num in A:
    sum += num

print(-sum)