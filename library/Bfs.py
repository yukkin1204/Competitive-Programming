# 幅優先探索 (BFS)
# ある頂点を始点として、そこから到達可能なすべての頂点への経路を探索する

# 状態の種類を定義
WHITE = 0
GRAY = 1
BLACK = 2

# 無限大を定義
INFTY = 2 ** 31 - 1

class Vertex:
    def __init__(self, id):
        self.id = id
        self.adj = set()
        self.color = WHITE
        self.dist = INFTY
        self.pred = None

    # 頂点の情報を表示
    def to_string(self):
        str_pred = "None"
        if self.pred != None:
            str_pred = str(self.pred)
        return f"{str(self.id)}, adj = {str(self.adj)}, color = {str(self.color)}, dist = {str(self.dist)}, pred = {str_pred}"

# 幅優先探索
def bfs (vertices, src):
    # 始点頂点の初期化
    src.color = GRAY
    src.dist = 0
    src.pred = None

    # 探索
    q = [src]
    while len(q) > 0:
        u = q.pop(0)
        for i in u.adj:
            v = vertices[i]
            if v.color == WHITE:
                v.color = GRAY
                v.dist = u.dist + 1
                v.pred = u.id
                q.append(v)
        u.color = BLACK

# 経路を表示
def print_path(vertices, src, v):
    if src.id == v.id:
        print(src.id, end = " ")
    elif v.pred == None:
        print("\n経路が存在しません")
    else:
        print_path(vertices, src, vertices[v.pred])
        print(v.id, end = " ")

# 頂点を接続
def connect(vertices, i, j):
    vertices[i].adj.add(j)

# --以下使用サンプル--

#頂点の数
N = 8

# 頂点の生成
vertices = []
for i in range(N):
    vertices.append(Vertex(i))

# 有向辺の設定
connect(vertices, 0, 1)
connect(vertices, 0, 7)
connect(vertices, 1, 0)
connect(vertices, 1, 2)
connect(vertices, 1, 6)
connect(vertices, 2, 1)
connect(vertices, 2, 3)
connect(vertices, 2, 5)
connect(vertices, 3, 2)
connect(vertices, 3, 4)
connect(vertices, 3, 5)
connect(vertices, 4, 3)
connect(vertices, 4, 5)
connect(vertices, 5, 2)
connect(vertices, 5, 3)
connect(vertices, 5, 4)
connect(vertices, 5, 6)
connect(vertices, 6, 1)
connect(vertices, 6, 5)
connect(vertices, 7, 0)

# 頂点3を始点として探索
bfs(vertices, vertices[3])

# 頂点3から頂点7への経路を表示
print("頂点3から頂点7への経路: ", end = "")
print_path(vertices, vertices[3], vertices[7])
print("")

# 各頂点の表示
for i in range(N):
    print(vertices[i].to_string())


