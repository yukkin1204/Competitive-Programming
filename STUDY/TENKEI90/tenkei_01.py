# Yokan Party
# 最小値の最大化問題は「答えの二分探索」で解けることが多い
N, L = map(int, input().split())
K = int(input())
A = list(map(int, input().split()))

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

left = 0
right = L
while right - left > 1:
    mid = left + (right - left) // 2
    if solve(mid):
        left = mid
    else:
        right = mid
print(left)

