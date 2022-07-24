# Trophy
# やりこむゲームは一種類なのがミソ
# やりこむゲームが一つ右にずれるごとに、sumがどう変化するかを追う
N, X = map(int,input().split())
l = []
for _ in range(N):
    A, B = map(int,input().split())
    l.append([A, B])

sum = l[0][0] + l[0][1] * X
min = sum

for i in range(N - 1):
    if X - (i + 1) < 0: break # ここの条件に注意
    sum += l[i + 1][0] + l[i + 1][1] * (X - (i + 1)) - l[i][1] * (X - (i + 1))
    if sum < min:
        min = sum

print(min)

