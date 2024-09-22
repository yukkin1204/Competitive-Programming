a, b, C = map(int, input().split())

C = str(bin(C)[2:])
c = C.count("1")

if (a + b - c) % 2 != 0 or a + b < c or b + c < a or c + a < b:
    print(-1)
    exit()

n = (a + b - c) // 2
C = "0" * max((n - (len(C) - c)), 0) + C
if len(C) > 60:
    print(-1)
    exit()

p = 0
X, Y = "", ""
X_count, Y_count = 0, 0

for char in C:
    if char == "0":
        if p < n:
            X += "1"
            X_count += 1
            Y += "1"
            Y_count += 1
            p += 1
        else:
            X += "0"
            Y += "0"
    else:
        if a - X_count > b - Y_count:
            X += "1"
            X_count += 1
            Y += "0"
        else:
            X += "0"
            Y += "1"
            Y_count += 1

print(int(X, 2), int(Y, 2))
