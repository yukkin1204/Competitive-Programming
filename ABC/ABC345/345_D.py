from itertools import combinations, permutations
from sys import stdin

N, H, W = map(int, input().split())
blocks = [list(map(int, stdin.readline().split())) for _ in range(N)]

def can_place(idx, muki):
    if idx == len(chosen_order):
        return True

    h, w = blocks[chosen_order[idx]]
    if muki:
        h, w = w, h
    start_i, start_j = 0, 0
    flg = False
    for i in range(H):
        for j in range(W):
            if m[i][j] == 0:
                start_i, start_j = i, j
                flg = True
                break
        if flg:
            break
    for di in range(h):
        for dj in range(w):
            if start_i + di >= H or start_j + dj >= W or m[start_i + di][start_j + dj] == 1:
                return False
    for di in range(h):
        for dj in range(w):
            m[start_i + di][start_j + dj] = 1
    idx += 1
    for muki in range(2):
        if can_place(idx, muki):
            return True

for i in range(1, N + 1):
    for chosen_blocks in combinations(range(N), i):
        if sum([blocks[x][0] * blocks[x][1] for x in chosen_blocks]) != H * W:
            continue
        for chosen_order in permutations(chosen_blocks):
            for muki in range(2):
                m = [[0] * W for _ in range(H)]
                idx = 0

                if can_place(idx, muki):
                    print("Yes")
                    exit()
print("No")