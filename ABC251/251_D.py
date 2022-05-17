# At Most 3 (Contestant ver.)
W = int(input())
l = []

for i in range(1, 101):
    l.append(i)
    l.append(i * 100)
    l.append(i * 10000)

print(len(l))
print(' '.join(map(str, l)))