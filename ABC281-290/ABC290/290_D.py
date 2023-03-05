# D - Marking
from sys import stdin
import math
T = int(input())
l = [list(map(int, stdin.readline().split())) for _ in range(T)]

for test in l:
    N, D, K = test[0], test[1], test[2]
    # 隣のマスをマーキングする周期
    period = N // math.gcd(N, D)
    # 隣のマスをマーキングする回数
    count = (K - 1) // period
    # 進んだ合計マス（mod N）
    print((D * (K - 1) + count) % N)
