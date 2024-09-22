# C - Circular Playlist
N, T = map(int, input().split())
A = list(map(int, input().split()))

r = T % sum(A)
sum = 0

for i in range(N):
    if sum + A[i] < r:
        sum += A[i]
    else:
        print(*[i + 1, r - sum])
        exit()
