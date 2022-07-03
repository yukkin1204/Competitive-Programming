# 答えで二分探索
# 題材は典型90問の01
N, L = map(int, input().split())
K = int(input())
A = list(map(int, input().split()))

# 二分探索で動かす変数の値がMの場合に、条件を満たすかどうかを返却する
def solve(M):
    count = 0
    start = 0
    for num in A:
        if num - start >= M and L - num >= M:
            count += 1
            start = num
    if count >= K:
        return True
    return False

# 二分探索
left = 0
right = L
while right - left > 1:
    mid = left + (right - left) // 2
    if solve(mid):
        # 最大値を求める問題ではleft=mid
        # 最小値を求める問題ではright=mid
        left = mid
    else:
        right = mid
# 最大値を求める問題ではleftが答え
# 最小値を求める問題ではrightが答え
print(left)