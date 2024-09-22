S = input()
l = [0] * 26

for char in S:
    l[ord(char) - 97] += 1

max = max(l)
max_index = l.index(max)
print(chr(max_index + 97))