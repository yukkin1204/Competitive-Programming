# D - Happy New Year 2023
# pとqのどちらかは9*10^18の3乗根以下であることがミソ
# 2以上のはじめに割り切れた数がpかqとなることから素数判定もしなくて良い
T = int(input())
test = [0] * T
for i in range(T):
    test[i] = int(input())

N = int((10 ** 18 * 9) ** (1 / 3))

for num in test:
    for i in range(2, N):
        if num % i == 0:
            # p=iのとき
            if (num // i) % i == 0:
                ans = [i, (num // i) // i]
            # q=iのとき
            else:
                ans = [int((num // i) ** (1 / 2)), i]
            break
    print(*ans)
