from sys import stdin
N = int(input())
P = list(map(int, input().split()))
Q = int(input())
l = [list(map(int, stdin.readline().split())) for _ in range(Q)]

for pair in l:
    A, B = pair[0], pair[1]
    id_a = P.index(A)
    id_b = P.index(B)
    if id_a < id_b:
        print(A)
    else:
        print(B)