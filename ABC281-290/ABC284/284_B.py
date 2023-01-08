# B - Multi Test Cases
T = int(input())
l = [0] * T

for i in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    count = 0
    for num in A:
        if num % 2 == 1:
            count += 1
    l[i] = count

print(*l, sep = "\n")