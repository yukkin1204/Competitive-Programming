# Jumping Takahashi 2
# 答えで二分探索
# ジャンプ力を決めると有向辺が貼られるのでBFSで解く
from sys import stdin

N = int(input())
l = [list(map(int, stdin.readline().split())) for _ in range(N)]
INFTY = 2 ** 31 - 1

def manhattan(i, j):
	return abs(l[i][0] - l[j][0]) + abs(l[i][1] - l[j][1])

# BFS
# 始点からすべての頂点に何手かで辿り着ければTrueを返す
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

    for num in dist:
        if num == INFTY:
            return False
    return True

def solve(M):
    graph = [[] for _ in range(N)]
    for i in range(N):
        for j in range(i + 1, N):
            if l[i][2] * M >= manhattan(i, j):
                graph[i].append(j)
            if l[j][2] * M >= manhattan(i, j):
                graph[j].append(i)

    for start in range(N):
        if bfs(start, graph):
            return True
    return False

left = 0
right = 10 ** 10 + 1
while right - left > 1:
    mid = left + (right - left) // 2
    if solve(mid):
        right = mid
    else:
        left = mid
print(right)
