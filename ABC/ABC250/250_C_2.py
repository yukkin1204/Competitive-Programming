# Adjacent Swaps
N, Q = map(int, input().split())
x = [int(input()) - 1 for i in range(Q)]
val = [i for i in range(N)]
pos = [i for i in range(N)]

for num in x:
    i = pos[num]
    if i != N - 1:
        val[i], val[i + 1] = val[i + 1], val[i]
        pos[val[i]], pos[val[i + 1]] = pos[val[i + 1]], pos[val[i]]
    else:
        val[i], val[i - 1] = val[i - 1], val[i]
        pos[val[i]], pos[val[i - 1]] = pos[val[i - 1]], pos[val[i]]

ans = map(lambda x: x + 1, val)
print(' '.join(map(str, ans)))
