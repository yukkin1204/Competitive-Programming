N, Q = map(int, input().split())

l = []
for i in range(N, 0, -1):
    l.append([i, 0])

for _ in range(Q):
    s, t = input().split()
    if s == "1":
        new_x, new_y = l[-1][0], l[-1][1]
        if t == "R":
            new_x += 1
        elif t == "L":
            new_x -= 1
        elif t == "U":
            new_y += 1
        else:
            new_y -= 1
        l.append([new_x, new_y])
    else:
        print(*l[-int(t)])
