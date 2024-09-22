S = input()

l = [[0] * 10 for _ in range(len(S) + 1)]

for i in range(1, len(S) + 1):
    l[i] = l[i - 1].copy()
    l[i][int(S[i - 1])] = (l[i][int(S[i - 1])] + 1) % 2

d = dict()
for row in l:
    s = ''.join(map(str, row))
    d[s] = d.get(s, 0) + 1

ans = 0
for val in d.values():
    ans += (val * (val - 1)) // 2

print(ans)
