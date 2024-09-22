# Ancestor
# 素直にwhile文でNから1まで親をたどり続ければ良い
N = int(input())
P = list(map(int, input().split()))

count = 1
x = P[N - 2]

while x > 1:
    x = P[x - 2]
    count += 1

print(count)
