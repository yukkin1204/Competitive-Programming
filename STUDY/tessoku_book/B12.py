# 解で二分探索
import math
N = int(input())

# 二分探索で動かす変数の値がmidの場合に、条件を満たすかどうかを返却する
def solve(mid):
    if mid ** 3 + mid <= N:
        return True
    return False

# 二分探索
ok = 0 # 解が存在する値
ng = math.ceil(N ** (1 / 3)) # 解が存在しない値
while abs(ok - ng) > 0.001:
    mid = (ok + ng) / 2
    if solve(mid):
        ok = mid
    else:
        ng = mid
print(ok)