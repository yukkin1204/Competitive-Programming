# LCM on Whiteboard
# 各素因数の最大個数が単独最大かを調べれば良い
from sys import stdin

N = int(input())
l = []
for i in range(N):
    mi = int(input())
    li = [list(map(int, stdin.readline().split())) for _ in range(mi)]
    l.append(li)

dict1 = dict() # 各素因数の最大個数を記録する ex) {7: 2, 2: 2, 5:1}
dict2 = dict() # 各素因数の個数が最大となるindexを記録する ex) {7: {0}, 2: {0}, 5: {0, 1}}

for i in range(N):
    for j in range(len(l[i])):
        # 素因数の最大個数の新規登録、または更新
        if l[i][j][0] not in dict1 or dict1[l[i][j][0]] < l[i][j][1]:
            dict1[l[i][j][0]] = l[i][j][1]
            dict2[l[i][j][0]] = [i]
        # 素因数の最大個数の同率1位を登録
        elif l[i][j][0] in dict1 and dict1[l[i][j][0]] == l[i][j][1]:
            dict2[l[i][j][0]].append(i)

indexSet = set()

for value in dict2.values():
    # 素因数の最大個数をもつindexが1つのとき(単独最大のとき)そのindexを集合に追加する
    if len(value) == 1:
        indexSet.add(value[0])

# 消しても影響のない数が1つでも存在する場合、1足したものが答えになることに注意
if len(indexSet) != N:
    print(len(indexSet) + 1)
else:
    print(len(indexSet))
