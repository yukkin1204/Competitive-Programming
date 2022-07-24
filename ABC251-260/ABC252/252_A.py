# ASCII code
# アスキーコードと英小文字リストを紐付け
import string
N = int(input())

l = list(string.ascii_lowercase)
print(l[N - 97])