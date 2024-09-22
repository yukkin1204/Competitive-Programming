# Takahashi's Failure
N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

max = 0
l = []

for i in range(N):
    if A[i] > max:
        max = A[i]
        l = []
        l.append(i + 1)
    elif A[i] == max:
        l.append(i + 1)

if len(set(B) & set(l)) > 0:
    print("Yes")
else:
    print("No")

