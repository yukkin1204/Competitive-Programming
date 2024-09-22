from sys import stdin
Q = int(input())
l = [list(map(int, stdin.readline().split())) for _ in range(Q)]
m = []

for pair in l:
    s, t = pair[0], pair[1]
    if s == 1:
        m.append(t)
    elif s == 2:
        print(m[-t])