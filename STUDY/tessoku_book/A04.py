# 2進法
N = int(input())

l = [0] * 10
for i in range(10):
    l[9 - i] = N % 2
    N = N // 2

print(*l, sep="")
