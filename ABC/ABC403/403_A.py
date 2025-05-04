N = int(input())
A = list(map(int, input().split()))

sum = 0

for i in range(N):
    if (i + 1) % 2 == 1:
        sum += A[i]

print(sum)
