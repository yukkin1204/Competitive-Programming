N, X = map(int, input().split())
A = set(map(int, input().split()))

for num in A:
    if num + X in A:
        print("Yes")
        exit()
print("No")