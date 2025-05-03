# -----巨大な数（最小値の初期値などに使う）-----
min = float("inf")


# -----素因数分解-----
# 入力 12
# 出力 [[2, 2], [3, 1]]
def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-(n**0.5) // 1)) + 1):
        if temp % i == 0:
            cnt = 0
            while temp % i == 0:
                cnt += 1
                temp //= i
            arr.append([i, cnt])
    if temp != 1:
        arr.append([temp, 1])
    return arr
