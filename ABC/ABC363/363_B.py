N, T, P = map(int, input().split())
L = list(map(int, input().split()))

for i in range(T):
    count = 0
    for num in L:
        if num + i >= T:
            count += 1
    if count >= P:
        print(i)
        exit()