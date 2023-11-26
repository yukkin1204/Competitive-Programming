import math
D = int(input())

ans = 2 ** 31 - 1
x_max = math.isqrt(D)
for x in range(x_max + 1):
    y_left = math.isqrt(D - x ** 2)
    y_right = y_left + 1
    tmp = min(abs(x ** 2 + y_left ** 2 - D), abs(x ** 2 + y_right ** 2 - D))
    if ans > tmp:
        ans = tmp
print(ans)
