# C - Max MEX
N, K = map(int, input().split())
A = set(map(int, input().split()))

count = 0

for i in range(K):
    if i in A:
        count += 1
    else:
        break

print(count)
