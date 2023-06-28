# 累積和（いもす法）
from sys import stdin
D = int(input())
N = int(input())
l = [list(map(int, stdin.readline().split())) for _ in range(N)]

diff = [0] * D
csum = [0]

for pair in l:
    diff[pair[0] - 1] += 1
    if pair[1] != D:
        diff[pair[1]] -= 1

for i in range(D):
    csum.append(csum[i] + diff[i])

print(*csum[1:], sep = "\n")