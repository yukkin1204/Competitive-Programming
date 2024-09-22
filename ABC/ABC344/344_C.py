N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))
L = int(input())
C = list(map(int, input().split()))
Q = int(input())
X = list(map(int, input().split()))

S = set()

for num_A in A:
    for num_B in B:
        for num_C in C:
            S.add(num_A + num_B + num_C)

for num_X in X:
    if num_X in S:
        print("Yes")
    else:
        print("No")
