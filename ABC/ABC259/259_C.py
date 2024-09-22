# XXtoXXX
S = list(input())
T = list(input())

A = []
B = []

# 文字列のランレングス圧縮を行う
# "aaabcc"→[["a",3],["b",1],["c",2]]
for i in range(len(S)):
    if i == 0 or S[i] != S[i - 1]:
        A.append([S[i], 1])
    else:
        A[-1][1] += 1

for i in range(len(T)):
    if i == 0 or T[i] != T[i - 1]:
        B.append([T[i], 1])
    else:
        B[-1][1] += 1

# 以下のいずれかの条件を満たす場合にNoとなる
# SとTの区間数が異なる
# SとTの文字が異なる区間が存在する
# Sの文字数が1でありTの文字数が1でない区間が存在する
# Sの文字数>Tの文字数の区間が存在する
if len(A) != len(B):
    print("No")
else:
    for i in range(len(A)):
        if (A[i][0] != B[i][0]) or (A[i][1] == 1 and B[i][1] != 1) or (A[i][1] > B[i][1]):
            print("No")
            exit()
    print("Yes")
