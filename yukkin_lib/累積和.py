'''
累積和
A[i]はi+1番目のデータ
S[0]=0, S[i]はA[i-1]まで(つまりi番目のデータまで)の総和
題材は鉄則A06
'''
from sys import stdin
N, Q = map(int, input().split())
A = list(map(int, input().split()))
l = [list(map(int, stdin.readline().split())) for _ in range(Q)]

S = [0] * (N + 1)
for i in range(N):
    S[i + 1] = S[i] + A[i]

for pair in l:
    print(S[pair[1]] - S[pair[0] - 1])