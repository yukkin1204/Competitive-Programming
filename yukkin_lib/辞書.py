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
d = Counter(l)  # Counter({3: 3, 1: 2, 2: 1})
d.most_common(2)  # Counter({3: 3, 1: 2}) カウント上位2位を取得
# Counter同士で足し算もできる
