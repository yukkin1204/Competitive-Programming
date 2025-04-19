Q = int(input())
l = [list(map(int, input().split())) for _ in range(Q)]
m = []

for row in l:
    if row[0] == 1:
        m.append(row[1])
    else:
        print(m.pop(0))
