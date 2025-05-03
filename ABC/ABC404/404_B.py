N = int(input())
S = [list(input()) for _ in range(N)]
T = [list(input()) for _ in range(N)]


def count_difference(matrix1, matrix2):
    return sum(matrix1[i][j] != matrix2[i][j] for i in range(N) for j in range(N))


def rotate(matrix):
    return [[matrix[N - j - 1][i] for j in range(N)] for i in range(N)]


def hoge(s, t):
    count = 0
    for i in range(N):
        for j in range(N):
            if s[i][j] != t[i][j]:
                count += 1
    return count


def rotate(s):
    new_s = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            new_s[i][j] = s[N - 1 - j][i]
    return new_s


min_cost = float("inf")
current = S

for rot in range(4):
    diff = count_difference(current, T)
    min_cost = min(min_cost, diff + rot)
    current = rotate(current)

print(min_cost)
