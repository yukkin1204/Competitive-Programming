import string

# アルファベット
# 小文字の出力 a-z
string.ascii_lowercase
# 大文字の出力 A-Z
string.ascii_uppercase

# 文字判定
# 小文字判定
"apple".islower()
# 大文字判定
"APPLE".isupper()
# 先頭大文字、その他は小文字
"Apple".istitle()

# 文字列のカウント
s = 'abc_aabbcc_abc'
print(s.count('abc'))

# 文字列変換
# 基本
"good".replace("oo", "o")
# 対応表
translation = str.maketrans("abc", "xyz")
"abcabc".translate(translation)

# 数値とアルファベットの変換
# 0→A
print(chr(0 + 65))
# 0→a
print(chr(0 + 97))
# A→0
print(ord('A') - 65)
# a→0
print(ord('a') - 97)

# 回文判定
word = "abcba"
word == word[::-1]