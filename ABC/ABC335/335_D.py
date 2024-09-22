N = int(input())

l = [[0] * N for _ in range(N)]
center = (N - 1) // 2
l[center][center] = "T"

y, x = 0, 0
muki = 0
v = [(0, 1), (1, 0), (0, -1), (-1, 0)]
num = 1

while y != center and x != center:
    while True:
        l[y][x] = num
        new_y, new_x = y + v[muki][0], x + v[muki][1]
        if new_y < 0 or new_y > N - 1 or new_x < 0 or new_x > N - 1 or l[new_y][new_x] != 0:
            break
        y, x = new_y, new_x
        num += 1
    muki = (muki + 1) % 4

for row in l:
    print(*row)
