# Circumferences
# 各円を頂点として考え、2円が交われば無向辺を貼る。そしてBFS
from sys import stdin

N = int(input())
sx, sy, tx, ty = map(int, input().split())
l = [list(map(int, stdin.readline().split())) for _ in range(N)]
INFTY = 2 ** 31 - 1

def bfs(s, g):
    dist = [INFTY] * N
    dist[s] = 0
    que = [s]

    while que:
        q = que.pop()
        for i in g[q]:
            if dist[i] != INFTY: continue
            dist[i] = dist[q] + 1
            que.append(i)

    return dist

# スタート点とゴール点がどの円周上にあるかを調べる
# 半径=2点間距離かどうか (2乗して調べる)
# 点が複数の円周上に存在することもあるが、そのうちどれか1つを取得できていれば問題ない
for i in range(N):
    if (l[i][0] - sx) ** 2 + (l[i][1] - sy) ** 2 == l[i][2] ** 2:
        s = i
    if (l[i][0] - tx) ** 2 + (l[i][1] - ty) ** 2 == l[i][2] ** 2:
        t = i

graph = [[] for _ in range(N)]

# 2円が交われば無向辺を貼る
for i in range(N):
    for j in range(i + 1, N):
        # 2円が交わる条件 (これも2乗して調べる)
        if (l[i][2] - l[j][2]) ** 2 <= (l[i][0] - l[j][0]) ** 2 + (l[i][1] - l[j][1]) ** 2 <= (l[i][2] + l[j][2]) ** 2:
            graph[i].append(j)
            graph[j].append(i)

dist = bfs(s, graph)

if dist[t] != INFTY:
    print("Yes")
else:
    print("No")
