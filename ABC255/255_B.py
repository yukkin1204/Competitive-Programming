# Light It Up
# NとKの全探索
# Nのパラメータごとに最小値を求め、その最大値が答え
from sys import stdin
N, K = map(int, input().split())
A = list(map(int, input().split()))
XY = [list(map(int, stdin.readline().split())) for _ in range(N)]

min_max = 0
for i in range(N):
    min = 10 ** 12
    for num in A:
        # 2乗で値をもっておき、最後に平方根を取る
        tmp = (XY[i][0] - XY[num - 1][0]) ** 2 + (XY[i][1] - XY[num - 1][1]) ** 2
        if tmp < min:
            min = tmp
    if min > min_max:
        min_max = min

print(min_max ** 0.5)
