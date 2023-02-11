# D - Step Up Robot
N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = set(map(int, input().split()))
X = int(input())

# 動的計画法
# dp[i]:i段目に登ることができるなら1、できないなら0
dp = [0] * (X + 1)
dp[0] = 1

for i in range(1, X + 1):
    if i not in B:
        for num in A:
            if i - num >= 0 and dp[i - num] == 1:
                dp[i] = 1

if dp[X] == 1:
    print("Yes")
else:
    print("No")
