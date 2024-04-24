'''
bit全探索
2択のN重ループでfor文をN個書くことを回避するテクニック
'''
# bit全探索
# 1, 3, 9, 27, 81の5つの数の和で表せる数を全て求める
l = [1, 3, 9, 27, 81]
N = len(l)
m = []

# 2択の5重ループ
for i in range(2 ** N):
    sum = 0
    for j in range(N):
        if (i >> j) & 1:
            sum += l[j]
    m.append(sum)

print(m)