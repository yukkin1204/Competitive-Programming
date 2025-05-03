from collections import Counter

# -----逆引き辞書（要素が含まれている行を返却）-----
l = [[1, 3], [1, 2], [3]]
d = {i: [] for i in range(1, 3 + 1)}
for i, row in enumerate(l):
    for num in row:
        d[num].append(i + 1)
# d = {1: [1, 2], 2: [2], 3: [1, 3]} となる

# -----Counter（要素のカウント一覧）-----
l = [1, 1, 2, 3, 3, 3]
d = Counter(l)
# d = Counter({3: 3, 1: 2, 2: 1}) となる
# d.most_common(n) でカウント上位n位を取得できる
# Counter同士で足し算ができる
