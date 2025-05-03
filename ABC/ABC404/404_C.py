from collections import defaultdict


class UnionFind:
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

    # x を含むグループのサイズを求める
    def size(self, x):
        return self.siz[self.root(x)]

    # x を含むグループの要素をリストで返す
    def members(self, x):
        root = self.root(x)
        return [i for i in range(1, self.n + 1) if self.root(i) == root]

    # グループの数を返す
    def group_count(self):
        return sum(x < 0 for x in self.par[1:])

    # {ルート要素: [そのグループに含まれる要素のリスト], ...}のdefaultdictを返す
    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(1, self.n + 1):
            group_members[self.root(member)].append(member)
        return group_members


N, M = map(int, input().split())
l = [list(map(int, input().split())) for _ in range(M)]

d = {i: 0 for i in range(1, N + 1)}
for A, B in l:
    d[A] += 1
    d[B] += 1

if any(d[i] != 2 for i in range(1, N + 1)):
    print("No")
    exit()

uf = UnionFind(N)

for A, B in l:
    uf.unite(A, B)

if uf.size(1) != N:
    print("No")
else:
    print("Yes")
