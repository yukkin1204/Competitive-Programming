from sys import stdin
N, Q = map(int, input().split())
A = list(map(int, input().split()))
l = [list(map(int, stdin.readline().split())) for _ in range(Q)]

sum_l = [0]
for i in range(N):
    sum_l.append(sum_l[i] + A[i])

for pair in l:
    print(sum_l[pair[1]] - sum_l[pair[0] - 1])
