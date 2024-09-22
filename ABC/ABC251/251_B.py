# At Most 3 (Judge ver.)
N, W = map(int, input().split())
A = list(map(int, input().split()))
S = set()

for i in range(0, N):
    if A[i] <= W:
        S.add(A[i])
    for j in range(i + 1, N):
        if A[i] + A[j] <= W:
            S.add(A[i] + A[j])
        for k in range(j + 1, N):
            if A[i] + A[j] + A[k] <= W:
                S.add(A[i] + A[j] + A[k])

print(len(S))