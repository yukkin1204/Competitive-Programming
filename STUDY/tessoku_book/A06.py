# 累積和
from sys import stdin
from itertools import accumulate
N, Q = map(int, input().split())
A = list(map(int, input().split()))
l = [list(map(int, stdin.readline().split())) for _ in range(Q)]

A = [0] + A
S = list(accumulate(A))
# 次と同義
# S = [0] * (N + 1)
# for i in range(N):
#     S[i + 1] = S[i] + A[i]

for pair in l:
    print(S[pair[1]] - S[pair[0] - 1])
