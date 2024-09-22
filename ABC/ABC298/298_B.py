from sys import stdin
import copy
N = int(input())
A = [list(map(int, stdin.readline().split())) for _ in range(N)]
B = [list(map(int, stdin.readline().split())) for _ in range(N)]

for _ in range(4):
    A_copy = copy.deepcopy(A)
    flg = True
    for i in range(N):
        for j in range(N):
            A[i][j] = A_copy[N - 1 - j][i]
            if A[i][j] == 1 and B[i][j] == 0:
                flg = False
    if flg:
        print("Yes")
        exit()

print("No")
