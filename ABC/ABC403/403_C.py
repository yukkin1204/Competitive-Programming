N, M, Q = map(int, input().split())
l = [list(map(int, input().split())) for _ in range(Q)]

d = {i: set() for i in range(N)}
m = [False] * N

for query in l:
    if query[0] == 1:
        d[query[1] - 1].add(query[2])
    elif query[0] == 2:
        m[query[1] - 1] = True
    else:
        if query[2] in d[query[1] - 1] or m[query[1] - 1]:
            print("Yes")
        else:
            print("No")
