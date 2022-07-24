# Just K
# bit全探索
import string

N, K = map(int, input().split())
l = [input() for l in range(N)]
m = []

for i in range(2 ** N):
    s = ""
    for j in range(N):
        if (i >> j) & 1:
            s += l[j]
    m.append(s)

max = 0

for str in m:
    count = 0
    for char in list(string.ascii_lowercase):
        if str.count(char) == K:
            count += 1
    if count > max:
        max = count

print(max)
