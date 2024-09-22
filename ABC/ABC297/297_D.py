A, B = map(int, input().split())

if A < B:
    A, B = B, A

count = 0

while B > 0:
    Q = A // B
    A = A - B * Q
    A, B = B, A
    count += Q

count -= 1

print(count)