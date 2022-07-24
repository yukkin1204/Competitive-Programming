# Longest Circular Road
# 木の直径+1が答えである
# 木の直径は最短距離計算2回で求めることができる
# 最大距離計算はBFSで行う
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

N = int(input())
graph = [[] for _ in range(N)]

for i in range(N - 1):
    a, b = map(int,input().split())
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)

dist1 = bfs(0, graph)
max_index = dist1.index(max(dist1))

dist2 = bfs(max_index, graph)
print(max(dist2) + 1)
