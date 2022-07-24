# Adjacent Swaps
N, Q = map(int, input().split())
x = [int(input()) for i in range(Q)]
val = [i + 1 for i in range(N)]
pos = [i + 1 for i in range(N)]

for num in x:
    i = pos[num - 1]
    if i != N:
        val[i - 1], val[i] = val[i], val[i - 1]
        pos[val[i - 1] - 1], pos[val[i] - 1] = pos[val[i] - 1], pos[val[i - 1] - 1]
    else:
        val[i - 1], val[i - 2] = val[i - 2], val[i - 1]
        pos[val[i - 1] - 1], pos[val[i - 2] - 1] = pos[val[i - 2] - 1], pos[val[i - 1] - 1]

print(' '.join(map(str, val)))
