# 二分探索
# 題材は典型90問の01
N, L = map(int, input().split())
K = int(input())
A = list(map(int, input().split()))

# 二分探索で動かす変数の値がMの場合に、条件を満たすかどうかを返却する
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

# 二分探索（最大値を求める）
left, right = 0, L
while right - left > 1:
    mid = (left + right) // 2
    if solve(mid):
        left = mid
    else:
        right = mid
print(left)

# 二分探索（最小値を求める）
# left, right = 0, L
# while right - left > 1:
#     mid = (left + right) // 2
#     if solve(mid):
#         right = mid
#     else:
#         left = mid
# print(right)