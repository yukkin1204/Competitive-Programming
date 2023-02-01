# B - Postal Card
from sys import stdin
N, M = map(int, input().split())
S = [stdin.readline()[:-1] for _ in range(N)]
T = set()
for _ in range(M):
    T.add(input())

count = 0
for str in S:
    if str[3:] in T:
        count += 1

print(count)

