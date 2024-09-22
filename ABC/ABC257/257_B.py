# 1D Pawn
# 移動によって、コマの位置関係は変わらないことがミソ
N, K, Q = map(int, input().split())
A = list(map(int, input().split()))
L = list(map(int, input().split()))

for num in L:
    if not (A[num - 1] == N or (num != K and A[num - 1] + 1 == A[num])):
        A[num - 1] += 1

print(' '.join(map(str, A)))
