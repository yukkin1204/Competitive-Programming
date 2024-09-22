# B - レ
from collections import deque
N, M = map(int, input().split())
A = set(map(int, input().split()))

ans = []
d = deque() # レ点でない整数に当たるまで一時保存

for i in range(1, N + 1):
    d.append(i)
    if i not in A:
        while d:
            ans.append(d.pop())

print(*ans)
