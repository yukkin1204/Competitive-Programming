# C - Count Connected Components
# C - Count Connected Components
# 連結成分の個数を求める問題
# すでにその頂点に訪れたかをN要素のBool配列で管理する
# すでに訪れている頂点→何もしない
# まだ訪れていない頂点→その頂点を始点にBFS、訪問実績の更新、count up
def bfs(s, g):
    dist = [2 ** 31 - 1] * N
    dist[s] = 0
    que = [s]

    while que:
        q = que.pop()
        for i in g[q]:
            if dist[i] != 2 ** 31 - 1: continue
            dist[i] = dist[q] + 1
            que.append(i)

    return dist

N, M = map(int, input().split())
graph = [[] for _ in range(N)]
for _ in range(M):
    u, v = map(int, input().split())
    graph[u - 1].append(v - 1)
    graph[v - 1].append(u - 1)

count = 0
l = [False] * N
for i in range(N):
    if not l[i]:
        dist = bfs(i, graph)
        for j in range(i, N):
            if dist[j] != 2 ** 31 - 1:
                l[j] = True
        count += 1

print(count)
