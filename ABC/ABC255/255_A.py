# You should output ARC, though this is ABC.
# 基礎問題
from sys import stdin
R, C = map(int, input().split())
l = [list(map(int, stdin.readline().split())) for _ in range(2)]

print(l[R - 1][C - 1])
