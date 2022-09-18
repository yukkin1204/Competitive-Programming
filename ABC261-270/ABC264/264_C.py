# Matrix Reducing
# どの行、どの列を残すかで全探索する (combinationを利用)
from sys import stdin
import itertools

H1, W1 = map(int, input().split())
A = [list(map(int, stdin.readline().split())) for _ in range(H1)]
H2, W2 = map(int, input().split())
B = [list(map(int, stdin.readline().split())) for _ in range(H2)]

l = list(itertools.combinations(range(H1), H2))
m = list(itertools.combinations(range(W1), W2))

for tuple_l in l:
    for tuple_m in m:
        flg = True
        for i, val_l in enumerate(tuple_l):
            if not flg:
                break
            for j, val_m in enumerate(tuple_m):
                if A[val_l][val_m] != B[i][j]:
                    flg = False
                    break
        if flg:
            print("Yes")
            exit()

print("No")
