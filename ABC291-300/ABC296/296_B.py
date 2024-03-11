from sys import stdin
S = [stdin.readline()[:-1] for _ in range(8)]

for i in range(8):
    if "*" in S[i]:
        idx = S[i].index("*")
        print(f"{chr(idx + 97)}{8 - i}")