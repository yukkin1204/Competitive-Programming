# 累積和
from sys import stdin
N, Q = map(int, input().split())
A = list(map(int, input().split()))
l = [list(map(int, stdin.readline().split())) for _ in range(Q)]

csum = [0]
for i in range(N):
    csum.append(csum[i] + A[i])

for pair in l:
    print(csum[pair[1]] - csum[pair[0] - 1])
