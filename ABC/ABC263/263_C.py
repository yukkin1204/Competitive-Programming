# Monotonically Increasing
# 組合せを出力するだけ
import itertools
N, M = map(int, input().split())

l = list(itertools.combinations(range(1, M + 1), N))
for tuple in l:
    print(*tuple)