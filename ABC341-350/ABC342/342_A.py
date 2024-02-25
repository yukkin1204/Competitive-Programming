S = input()
n = len(S)

for i in range(n):
    flg = True
    for j in range(n):
        if i != j and S[i] == S[j]:
            flg = False
            break
    if flg:
        print(i + 1)
