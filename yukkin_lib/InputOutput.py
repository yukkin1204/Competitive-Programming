from sys import stdin
import string

# -----Input-----

# 整数が1つ書かれた行
n = int(input())
# 整数が複数書かれた行
m, n = map(int, input().split())
l = list(map(int, input().split()))
# 整数が複数書かれた複数行
l = [list(map(int, stdin.readline().split())) for _ in range(n)]

# 文字列が1つ書かれた行
s = input()
# 文字列が書かれた複数行
l = [stdin.readline()[:-1] for _ in range(n)]

# -----Output-----

# 1つ出力
print(s)
# 空白区切りで複数出力
print(*l)
# 改行区切りで複数出力
print(*l, sep = "\n")

# -----List-----

# 1次元リスト
l = [0] * n
# 2次元リスト
l = [[0] * m for _ in range(n)]
l = [[] for _ in range(n)]

# -----Alphabet------

# abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.ascii_letters)
# abcdefghijklmnopqrstuvwxyz
print(string.ascii_lowercase)
# ABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.ascii_uppercase)
