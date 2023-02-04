# Qualification Contest
from sys import stdin
N, K = map(int, input().split())
S = [stdin.readline()[:-1] for _ in range(N)]

S = S[0:K]
S = sorted(S)
print(*S, sep = "\n")
