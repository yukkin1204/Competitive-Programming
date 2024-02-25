import math
N, M, K = map(int, input().split())
L = math.lcm(N, M)

def solve(mid):
    return mid // N + mid // M - mid // L * 2 >= K

left, right = 0, 10 ** 20
while right - left > 1:
    mid = (left + right) // 2
    if solve(mid):
        right = mid
    else:
        left = mid
print(right)