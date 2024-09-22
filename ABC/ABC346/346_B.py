W, B = map(int, input().split())

s = "wbwbwwbwbwbw"
for i in range(12):
    w, b = 0, 0
    for j in range(W + B):
        if s[(i + j) % 12] == 'w':
            w += 1
        else:
            b += 1
    if W == w and B == b:
        print("Yes")
        exit()
print("No")
