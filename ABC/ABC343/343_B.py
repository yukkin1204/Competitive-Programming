N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]

for row in A:
    l = []
    for i in range(N):
        if row[i] == 1:
            l.append(i + 1)
    print(*l)