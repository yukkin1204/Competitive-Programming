# B - Yellow and Red Card
from sys import stdin
N, Q = map(int, input().split())
l = [list(map(int, stdin.readline().split())) for _ in range(Q)]

s = [0] * N

for event in l:
    a, x = event[0], event[1]
    if  a == 1:
        s[x - 1] += 1
    elif a == 2:
        s[x - 1] += 2
    else:
        if s[x - 1] >= 2:
            print("Yes")
        else:
            print("No")
