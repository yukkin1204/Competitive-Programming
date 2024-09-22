from sys import stdin
N = int(input())
l = [stdin.readline()[:-1] for _ in range(N)]

left = -1
right = -1
hirou = 0

for row in l:
    A, S = row.split()
    if S == "L":
        if left != -1:
            hirou += abs(left - int(A))
        left = int(A)
    else:
        if right != -1:
            hirou += abs(right - int(A))
        right = int(A)

print(hirou)
