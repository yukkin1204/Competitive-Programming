# A - Sequence of Strings
from sys import stdin
N = int(input())
S = [stdin.readline()[:-1] for _ in range(N)]
S.reverse()
print(*S, sep = "\n")