N = int(input())
A = list(map(int, input().split()))

B = [0] * (N - 1)
for i in range(N - 1):
    B[i] = A[i + 1] - A[i]

count = N
rensa = 1

for i in range(N - 1):
    if i == N - 2:
        count += rensa * (rensa + 1) // 2
    elif B[i + 1] == B[i]:
        rensa += 1
    else:
        count += rensa * (rensa + 1) // 2
        rensa = 1

print(count)
