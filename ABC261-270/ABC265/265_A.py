# A - Apple
X, Y, N = map(int, input().split())
print(min((N // 3) * Y + (N % 3) * X, N * X))