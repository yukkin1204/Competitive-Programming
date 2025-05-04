import string
from collections import Counter
from itertools import groupby

# -----アルファベット-----
# 小文字の出力 a-z
string.ascii_lowercase  # abc…z
# 大文字の出力 A-Z
string.ascii_uppercase  # ABC…Z


# -----大文字小文字判定-----
# 小文字判定
"apple".islower()
# 大文字判定
"APPLE".isupper()
# 先頭大文字、その他は小文字
"Apple".istitle()


# -----カウント-----
s = "abcaabbccabc"
# 指定の文字列が何回登場するかカウント
s.count("abc")  # 2
# 各文字が何回登場するかカウント
Counter(s)  # Counter({'a': 4, 'b': 4, 'c': 4})


# -----文字列の存在判定-----
"abc" in "xxabcxx"

# -----文字列変換-----
# 部分文字列単位の変換
"good".replace("oo", "o")  # god
# 一文字単位の変換
translation = str.maketrans("abc", "xyz")  # 文字の対応表
print("abcb".translate(translation))  # xyzy


# -----数値と文字列変換-----
# 0→A
print(chr(0 + 65))
# 0→a
print(chr(0 + 97))
# A→0
print(ord("A") - 65)
# a→0
print(ord("a") - 97)


# -----回文判定-----
word = "abcba"
word == word[::-1]


# ------ランレングス圧縮----
# "aabbbbaaca" -> [('a', 2), ('b', 4), ('a', 2), ('c', 1), ('a', 1)]
def runLengthEncode(S):
    res = []
    for k, v in groupby(S):
        res.append((k, len(list(v))))
    return res


# [('a', 2), ('b', 4), ('a', 2), ('c', 1), ('a', 1)] -> "aabbbbaaca"
def runLengthDecode(L):
    res_list = []
    for c, n in L:
        res_list.append(c * int(n))
    return "".join(res_list)
