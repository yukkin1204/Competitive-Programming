# Triangle (Easier)
# グラフの連結状況を行列で保存
N, M = map(int, input().split())

l = [[0] * N for _ in range(N)]
for _ in range(M):
    U, V = map(int, input().split())
    l[U - 1][V - 1] = 1
    l[V - 1][U - 1] = 1

count = 0

for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            if l[i][j] == 1 and l[j][k] == 1 and l[k][i] == 1:
                count += 1

print(count)
