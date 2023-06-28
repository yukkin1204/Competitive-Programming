# D - Tying Rope
class UnionFind():
    # 初期化
    def __init__(self, n):
        self.n = n
        self.par = [-1] * (n + 1)
        self.rank = [0] * (n + 1)
        self.siz = [1] * (n + 1)

    # 根を求める
    def root(self, x):
        if self.par[x] == -1:
            return x
        else:
            self.par[x] = self.root(self.par[x])
            return self.par[x]

    # x と y が同じグループに属するか (根が一致するか)
    def issame(self, x, y):
        return self.root(x) == self.root(y)

    # x を含むグループと y を含むグループを併合する
    def unite(self, x, y):
        rx = self.root(x)
        ry = self.root(y)
        if rx == ry:
            return False
        if self.rank[rx] < self.rank[ry]:
            rx, ry = ry, rx
        self.par[ry] = rx
        if self.rank[rx] == self.rank[ry]:
            self.rank[rx] += 1
        self.siz[rx] += self.siz[ry]
        return True

    # グループの数を返す
    def group_count(self):
        return sum(x < 0 for x in self.par[1:])

N, M = map(int, input().split())
uf = UnionFind(N)
count = 0

for _ in range(M):
    A, B, C, D = input().split()
    if uf.issame(int(A), int(C)):
        count += 1
    else:
        uf.unite(int(A), int(C))

print(count, uf.group_count() - count)
