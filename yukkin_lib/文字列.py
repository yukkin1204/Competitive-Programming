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

# 文字列変換
# 基本
"good".replace("oo", "o")
# 対応表
translation = str.maketrans("abc", "xyz")
"abcabc".translate(translation)