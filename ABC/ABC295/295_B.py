from sys import stdin
import copy
R, C = map(int, input().split())
B = [list(stdin.readline()[:-1]) for _ in range(R)]
ans = copy.deepcopy(B)

for i in range(R):
    for j in range(C):
        if B[i][j].isnumeric():
            for k in range(R):
                for l in range(C):
                    if abs(i - k) + abs(j - l) <= int(B[i][j]):
                        ans[k][l] = "."

for row in ans:
    print(*row, sep="")