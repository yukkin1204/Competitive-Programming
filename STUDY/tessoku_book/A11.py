# 二分探索
N, X = map(int, input().split())
A = list(map(int, input().split()))

ok = 0 # 解が存在する値
ng = N # 解が存在しない値
while abs(ok - ng) > 1:
    mid = (ok + ng) // 2
    if A[mid] <= X:
        ok = mid
    else:
        ng = mid
print(ok + 1)
