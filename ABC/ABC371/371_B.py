N, M = map(int, input().split())

l = [False] * N

for _ in range(M):
  A, B = input().split()
  if l[int(A) - 1] == False and B == "M":
    l[int(A) - 1] = True
    print("Yes")
  else:
    print("No")
