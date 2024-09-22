import string
S = input()
n = len(S)

d = {i: 0 for i in string.ascii_lowercase}
for char in S:
    d[char] += 1

count = n * (n - 1) // 2
flg = False
for char in d:
    if d[char] >= 2:
        count -= (d[char] * (d[char] - 1)) // 2
        flg = True
if flg:
    count += 1

print(count)
