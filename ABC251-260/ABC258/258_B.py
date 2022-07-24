# Number Box
# 全マス・全方向の全探索で解ける
N = int(input())
A = [list(map(int, list(input()))) for _ in range(N)]

max = 0
# 8方向を情報として持っておく
l = [(1, 1), (1, 0), (1, -1), (0, 1), (0, -1), (-1, 1), (-1, 0), (-1, -1)]

for i in range(N):
    for j in range(N):
        for pair in l:
            # 0から始めて10倍して足すの繰り返し
            num = 0
            for k in range(N):
                num *= 10
                # 1とNが隣接していることはmodNを考えることで対処
                num += A[(i + k * pair[0]) % N][(j + k * pair[1]) % N]
            if num > max:
                max = num

print(max)
