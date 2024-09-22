from sys import stdin
Q = int(input())
l = [list(map(int, stdin.readline().split())) for _ in range(Q)]

S = 1
n = 1
mod = 998244353

for query in l:
    if query[0] == 1:
        S = 10 * S + query[1]
    elif query[0] == 2:
        S %= pow(10, len(str(S)) - 1)
    else:
        print(S % mod)
