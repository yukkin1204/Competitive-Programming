# -----Input-----

# 整数
# 【1行】1数字
n = int(input())
# 【1行】複数数字
a, b, c = map(int, input().split())
l = list(map(int, input().split()))
# 【複数行】1数字
l = [int(input()) for _ in range(n)]
# 【複数行】複数数字
l = [list(map(int, input().split())) for _ in range(n)]

# 文字列
# 【1行】1単語
s = input()
# 【1行】複数単語
a,b,c = input().split()
l = list(input().split())
# 【複数行】1単語
l = [input() for _ in range(n)]
# 【複数行】複数単語
l = [list(input().split()) for _ in range(n)]

# -----Output-----

# 1つ出力
print(s)
# 空白区切りで複数出力
print(*l)
# 区切り文字なしで複数出力
print(*l, sep="")
# 改行区切りで複数出力
print(*l, sep = "\n")
