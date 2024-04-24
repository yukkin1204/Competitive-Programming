'''
二分探索 (めぐる式二分探索)
全探索だとO(N)のものをO(logN)にするテクニック
条件を満たす値の最小値や最大値を調べる問題で有効
okとngの初期値設定と、solve関数をいじるだけで使える
題材は典型90問の01
'''
N, L = map(int, input().split())
K = int(input())
A = list(map(int, input().split()))

# 二分探索で動かす変数の値がmidの場合に、条件を満たすかどうかを返却する
def solve(mid):
    count = 0
    start = 0
    for num in A:
        if num - start >= mid and L - num >= mid:
            count += 1
            start = num
    if count >= K:
        return True
    return False

# 二分探索
ok = 1 # 解が存在する値
ng = L # 解が存在しない値
while abs(ok - ng) > 1:
    mid = (ok + ng) // 2
    if solve(mid):
        ok = mid
    else:
        ng = mid
print(ok)
