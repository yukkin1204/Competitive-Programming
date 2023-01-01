from sys import stdin
N, M = map(int, input().split())
S = [stdin.readline()[:-1] for _ in range(N)]

count = 0

for i in range(N):
    for j in range(i + 1 , N):
        flg = True
        for k in range(M):
            if (S[i][k] == 'x' and S[j][k] == 'x'):
                flg = False
                break
        if flg:
            count += 1

print(count)
