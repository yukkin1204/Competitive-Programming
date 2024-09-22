l = []

while True:
    A = int(input())
    l.append(A)
    if A == 0:
        break

n = len(l)
for i in range(n):
    print(l[n - 1 - i])
