# B - First Query Problem
from sys import stdin
N = int(input())
A = list(map(int, input().split()))
Q = int(input())
l = [list(map(int, stdin.readline().split())) for _ in range(Q)]

for obj in l:
    if obj[0] == 1:
        A[obj[1] - 1] = obj[2]
    else:
        print(A[obj[1] - 1])
