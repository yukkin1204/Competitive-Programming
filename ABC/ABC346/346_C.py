N, K = map(int, input().split())
A = set(map(int, input().split()))

sum = K * (K + 1) // 2
for num in A:
    if num <= K:
        sum -= num

print(sum)