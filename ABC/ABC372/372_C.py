N, Q = map(int, input().split())
S = list(input())
count = 0

for i in range(N - 2):
    if S[i:i + 3] == ["A", "B", "C"]:
        count += 1

for _ in range(Q):
    X, C = input().split()
    index = int(X) - 1

    # 変更箇所の前後2文字を調査範囲とすることで時間削減
    for i in range(max(0, index - 2), min(N - 2, index + 1)):
        if S[i:i + 3] == ["A", "B", "C"]:
            count -= 1

    S[index] = C

    for i in range(max(0, index - 2), min(N - 2, index + 1)):
        if S[i:i + 3] == ["A", "B", "C"]:
            count += 1

    print(count)
