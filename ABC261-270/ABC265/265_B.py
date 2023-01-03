# B - Explore
N, M, T = map(int, input().split())
A = list(map(int, input().split()))
d = dict()
for _ in range(M):
    X, Y = map(int, input().split())
    d[X] = Y

for i in range(N - 1):
    if T - A[i] <= 0:
        print("No")
        exit()
    else:
        T -= A[i]
        if i + 2 in d:
            T += d[i + 2]

print("Yes")
