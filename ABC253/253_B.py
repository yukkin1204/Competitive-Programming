# Distance Between Tokens
# 2点が何マス離れているかを求める。全探索
H, W = map(int, input().split())
l = [list(list(input())) for i in range(H)]

X = []
Y = []

for i in range(H):
    for j in range(W):
        if l[i][j] == "o":
            X.append(i)
            Y.append(j)

print(abs(X[0] - X[1]) + abs(Y[0] - Y[1]))
