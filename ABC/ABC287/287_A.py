# A - Majority
from sys import stdin
N = int(input())
S = [stdin.readline()[:-1] for _ in range(N)]

if S.count("For") > S.count("Against"):
    print("Yes")
else:
    print("No")
