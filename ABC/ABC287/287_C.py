# C - Path Graph?
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

N, M = map(int, input().split())
graph = [[] for _ in range(N)]
for _ in range(M):
    u, v = map(int, input().split())
    graph[u - 1].append(v - 1)
    graph[v - 1].append(u - 1)

# まず一度bfsをして端点候補を求める
dist_1 = bfs(0, graph)
max_index = dist_1.index(max(dist_1))
# 端点で再度BFS
dist_2 = bfs(max_index, graph)
# 並び替えたものが[0, 1, 2, ... , N - 1]であればOK
dist_2 = sorted(dist_2)

for i in range(N - 1):
    if dist_2[i + 1] != dist_2[i] + 1:
        print("No")
        exit()

print("Yes")
