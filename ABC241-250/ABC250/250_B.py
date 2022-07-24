# Enlarged Checker Board
N, A, B = map(int, input().split())

for i in range(N):
    for j in range(A):
        str = ""
        for k in range(N):
            if (i + k) % 2 == 0:
                str += "." * B
            else:
                str += "#" * B
        print(str)
