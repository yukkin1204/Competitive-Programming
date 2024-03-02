import math
N = int(input())

n = math.ceil(N ** (1 / 3)) + 1 # 誤差を見越して切り上げ
for i in reversed(range(1, n + 1)):
    word = str(i ** 3)
    if i ** 3 <= N and word == word[::-1]:
        print(i ** 3)
        exit()