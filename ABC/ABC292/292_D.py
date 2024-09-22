# D - Unicyclic Components
from sys import stdin

class UnionFind():
    # 初期化
    def __init__(self, n):
        self.n = n
        self.par = [-1] * (n + 1)
        self.rank = [0] * (n + 1)
        self.siz = [1] * (n + 1)
        self.edg = [0] * (n + 1)

    # 根を求める
    def root(self, x):
        if self.par[x] == -1:
            return x
        else:
            self.par[x] = self.root(self.par[x])
            return self.par[x]

    # x を含むグループと y を含むグループを併合する
    def unite(self, x, y):
        rx = self.root(x)
        ry = self.root(y)
        if rx == ry:
            self.edg[rx] += 1
            return False
        if self.rank[rx] < self.rank[ry]:
            rx, ry = ry, rx
        self.par[ry] = rx
        if self.rank[rx] == self.rank[ry]:
            self.rank[rx] += 1
        self.siz[rx] += self.siz[ry]
        self.edg[rx] += self.edg[ry] + 1
        return True

    # x を含むグループの頂点の個数を求める
    def size(self, x):
        return self.siz[self.root(x)]

    # x を含むグループの辺の本数を求める
    def edge(self, x):
        return self.edg[self.root(x)]

N, M = map(int, input().split())
l = [list(map(int, stdin.readline().split())) for _ in range(M)]

uf = UnionFind(N)
for edge in l:
    uf.unite(edge[0], edge[1])

for i in range(1, N + 1):
    if uf.size(i) != uf.edge(i):
        print("No")
        exit()
print("Yes")
