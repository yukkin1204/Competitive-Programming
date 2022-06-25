# Robot Takahashi
# 体重でソートし、仕切りを一つずつずらした時にf(X)の値がどう変動するかに着目

N = int(input())
S = list(input())
W = list(map(int, input().split()))

f_x = S.count('1')
max = f_x

l = list(zip(S, W)) # 2つの配列をペアリング
l.sort(key = lambda x: x[1]) # W側でソート

for i in range(N):
    # ここがミソ
    if l[i][0] == "0":
        f_x += 1
    else:
        f_x -= 1
    # 次の数が異なる値ならば、現在のf(X)がmaxであるかどうかを判定する
    if (i == N - 1 or l[i][1] != l[i + 1][1]):
        if (f_x > max):
            max = f_x

print(max)
