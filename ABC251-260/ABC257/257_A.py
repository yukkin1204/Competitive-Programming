# A to Z String 2
# 基礎問題
import string
N, X = map(int, input().split())

q = X // N
r = X % N
l = list(string.ascii_uppercase) # 英大文字のリスト

if r == 0:
    print(l[q - 1])
else:
    print(l[q])
