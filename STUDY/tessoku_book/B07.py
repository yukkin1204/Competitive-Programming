# 累積和（いもす法）
from sys import stdin
T = int(input())
N = int(input())
l = [list(map(int, stdin.readline().split())) for _ in range(N)]

diff = [0] * T
csum = [0]

# 時刻2〜5に勤務の場合、時刻2.5（idでは2）に+1、時刻5.5（idでは5）に-1する
for pair in l:
    diff[pair[0]] += 1
    if pair[1] != T:
        diff[pair[1]] -= 1

for i in range(T):
    csum.append(csum[i] + diff[i])

print(*csum[1:], sep = "\n")