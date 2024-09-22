# Filling 3x3 array
# 9マス中4マス確定すれば残りは決まることがポイント
h_1, h_2, h_3, w_1, w_2, w_3 = map(int, input().split())

count = 0

for a in range(1, h_1 - 1):
    for b in range(1, h_1 - a):
        for d in range(1, w_1 - a):
            for e in range(1, w_2 - b):
                c = h_1 - a - b
                f = h_2 - d - e
                g = w_1 - a - d
                h = w_2 - b - e
                i = w_3 - c - f
                if (f > 0 and i > 0 and g + h + i == h_3):
                    count += 1

print(count)
