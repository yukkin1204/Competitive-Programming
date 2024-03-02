N, T = map(int, input().split())

P = [0] * N
d = {0: N}

for _ in range(T):
    A, B = map(int, input().split())

    d[P[A - 1]] -= 1
    if d[P[A - 1]] == 0:
        del d[P[A - 1]]

    P[A - 1] += B

    if P[A - 1] not in d.keys():
        d[P[A - 1]] = 1
    else:
        d[P[A - 1]] += 1

    print(len(d.keys()))
