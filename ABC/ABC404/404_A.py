import string

S = input()

for char in string.ascii_lowercase:
    if char not in S:
        print(char)
        exit()
