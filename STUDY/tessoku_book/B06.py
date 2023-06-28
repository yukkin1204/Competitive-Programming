from sys import stdin
N = int(input())
A = list(map(int, input().split()))
Q = int(input())
l = [list(map(int, stdin.readline().split())) for _ in range(Q)]

csum_1 = [0]
csum_0 = [0]
# 累積和
for i in range(N):
    if A[i] == 1:
        csum_1.append(csum_1[i] + 1)
        csum_0.append(csum_0[i])
    else:
        csum_1.append(csum_1[i])
        csum_0.append(csum_0[i] + 1)

for pair in l:
    if csum_1[pair[1]] - csum_1[pair[0] - 1] > csum_0[pair[1]] - csum_0[pair[0] - 1]:
        print('win')
    elif csum_1[pair[1]] - csum_1[pair[0] - 1] < csum_0[pair[1]] - csum_0[pair[0] - 1]:
        print('lose')
    else:
        print('draw')
