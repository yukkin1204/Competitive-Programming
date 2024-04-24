# 二分探索
N = int(input())
A = list(map(int, input().split()))
Q = int(input())
X = []
for _ in range(Q):
    X.append(int(input()))

A.sort()

for num in X:
    ok = -1 # 解が存在する値
    ng = N # 解が存在しない値
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if A[mid] < num:
            ok = mid
        else:
            ng = mid
    print(ok + 1)