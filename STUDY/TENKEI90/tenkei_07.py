# CP Classes
# ソートして二分探索
# bisect_leftでリストのどの箇所に挿入するべきかを調べられる
# 挿入候補が複数ある場合は左側を優先 (bisect_rightは右側を優先)
from bisect import bisect_left

N = int(input())
A = list(map(int, input().split()))
Q = int(input())

# 計算量 O(NlogN)
A.sort()

# 計算量 O(logN)がQ回のため、O(QlogN)
for _ in range(Q):
    B = int(input())
    idx = bisect_left(A, B)
    if idx == 0:
        ans = abs(B - A[idx])
    elif idx == N:
        ans = abs(B - A[idx - 1])
    else:
        ans = min(abs(B - A[idx - 1]),abs(B - A[idx]))
    print(ans)
