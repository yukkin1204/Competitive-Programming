# "redocta".swap(i,i+1)
# 左から一文字ずつ確定させれば良い
# "redocta"のaを一番左端に持っていくのに必要な手数は、aのindexと同じであることを利用する
# 確定した文字は除去する
S = input()

count = 0
for char in "atcoder":
    count += S.index(char)
    S = S.replace(char, "")
print(count)