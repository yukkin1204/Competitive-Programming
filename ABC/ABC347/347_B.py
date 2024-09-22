S = input()
n = len(S)
s = set()

for i in range(n):
    for j in range(n - i):
        s.add(S[j : j + i + 1])
print(len(s))