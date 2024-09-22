# B - Call the ID Number
N = int(input())
A = list(map(int, input().split()))

S = set()

for i in range(N):
    if not i + 1 in S:
        S.add(A[i])

ans = set(range(1, N + 1)) - S
print(len(ans))
print(*ans)
