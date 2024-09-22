N = int(input())
l = []
for i in range(N):
    l.append(list(input()))

m = []
for i in range(N):
    cnt = l[i].count("P")
    if cnt >= 1:
        j = l[i].index("P")
        m.append([j, i])
    if cnt == 2:
        j = list(reversed(l[i])).index("P")
        m.append([N - 1 - j, i])

x_1, y_1, x_2, y_2 = m[0][0], m[0][1], m[1][0], m[1][1]

def up(x_1, y_1, x_2, y_2):
    count = 0
    while True:
        if (y_1 == 0 or l[y_1 - 1][x_1] == "#") and (y_2 == 0 or l[y_2 - 1][x_2] == "#"):
            return x_1, y_1, x_2, y_2, count
        else:
            if (y_1 != 0 and l[y_1 - 1][x_1] != "#"):
                y_1 -= 1
            if (y_2 != 0 and l[y_2 - 1][x_2] != "#"):
                y_2 -= 1
            count += 1

def down(x_1, y_1, x_2, y_2):
    count = 0
    while True:
        if (y_1 == N - 1 or l[y_1 + 1][x_1] == "#") and (y_2 == N - 1 or l[y_2 + 1][x_2] == "#"):
            return x_1, y_1, x_2, y_2, count
        else:
            if (y_1 != N - 1 and l[y_1 + 1][x_1] != "#"):
                y_1 += 1
            if (y_2 != N - 1 and l[y_2 + 1][x_2] != "#"):
                y_2 += 1
            count += 1

def right(x_1, y_1, x_2, y_2):
    count = 0
    while True:
        if (x_1 == N - 1 or l[y_1][x_1 + 1] == "#") and (x_2 == N - 1 or l[y_2][x_2 + 1] == "#"):
            return x_1, y_1, x_2, y_2, count
        else:
            if (x_1 != N - 1 and l[y_1][x_1 + 1] != "#"):
                x_1 += 1
            if (x_2 != N - 1 and l[y_2][x_2 + 1] != "#"):
                x_2 += 1
        count += 1

def left(x_1, y_1, x_2, y_2):
    while True:
        count = 0
        if (x_1 == 0 or l[y_1][x_1 - 1] == "#") and (x_2 == 0 or l[y_2][x_2 - 1] == "#"):
            return x_1, y_1, x_2, y_2, count
        else:
            if (x_1 != 0 and l[y_1][x_1 - 1] != "#"):
                x_1 -= 1
            if (x_2 != 0 and l[y_2][x_2 - 1] != "#"):
                x_2 -= 1
        count += 1

