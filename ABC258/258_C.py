# Rotation
# 文字列のローテーション
# 移動回数と余りに着目するのがミソ
N, Q = map(int,input().split())
S = list(input())
dict = dict()

for i in range(len(S)):
    dict[i] = S[i]

count = 0
for _ in range(Q):
    t, x = map(int,input().split())
    if t == 1:
        count += x
    else:
        print(dict[(x - 1 - count) % N])







