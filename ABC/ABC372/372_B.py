M = int(input())

A = []

while M > 0:
  for i in range(10, -1, -1):
    if 3 ** i <= M:
      A.append(i)
      M -= 3 ** i
      break

print(len(A))
print(*A)
