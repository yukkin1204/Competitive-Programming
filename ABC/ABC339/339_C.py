N = int(input())
A = list(map(int, input().split()))

csum = [0]
for i in range(N):
    csum.append(csum[i] + A[i])

min = min(csum)
if min < 0:
    print(csum[-1] - min)
else:
    print(csum[-1])