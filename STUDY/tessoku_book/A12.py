# 解で二分探索
N, K = map(int, input().split())
A = list(map(int, input().split()))

# 二分探索で動かす変数の値がmidの場合に、条件を満たすかどうかを返却する
def solve(mid):
    count = 0
    for num in A:
        count += mid // num
    if count >= K:
        return True
    return False

# 二分探索
ok = 10 ** 9 # 解が存在する値
ng = 0 # 解が存在しない値
while abs(ok - ng) > 1:
    mid = (ok + ng) // 2
    if solve(mid):
        ok = mid
    else:
        ng = mid
print(ok)