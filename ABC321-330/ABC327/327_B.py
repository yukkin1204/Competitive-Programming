B = int(input())
A = 1
while A ** A <= B:
    if A ** A == B:
        print(A)
        exit()
    else:
        A += 1
print(-1)