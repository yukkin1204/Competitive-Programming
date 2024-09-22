import string
S = input()

alphabets = {i: 0 for i in string.ascii_lowercase}

for i in S:
    if i in alphabets:
        alphabets[i] += 1


d = dict()
for k, v in alphabets.items():
    if v in d:
        d[v] += 1
    else:
        d[v] = 1

for k, v in d.items():
    if k != 0 and v != 0 and v != 2:
        print("No")
        exit()
print("Yes")