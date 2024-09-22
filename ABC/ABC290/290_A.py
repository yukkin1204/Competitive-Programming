# A - Contest Result
N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

score = 0
for num in B:
    score += A[num - 1]
print(score)
