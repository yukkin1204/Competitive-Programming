# NewFolder(1)
N = int(input())
d = dict() # 各文字列の出現回数を記録する ex) {newfile: 2, newfolder: 1}

for _ in range(N):
    S = input()
    if S in d:
        print(f"{S}({d[S]})")
        d[S] += 1
    else:
        print(S)
        d[S] = 1
