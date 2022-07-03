# 幅優先探索 (BFS)
# ある頂点を始点として、そこから到達可能なすべての頂点を探索する

def bfs(s, g):
    INFTY = 2 ** 31 - 1
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

# --以下使用サンプル--
N = int(input())
graph = [[] for _ in range(N)]
graph[0].append(1) # 有向辺の設定
dist = bfs(0, graph) # 各頂点が始点から何手で行けるかを返却