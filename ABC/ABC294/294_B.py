from sys import stdin
import string
H, W = map(int, input().split())
l = [list(map(int, stdin.readline().split())) for _ in range(H)]

str = "." + string.ascii_uppercase

for row in l:
    ans = [str[i] for i in row]
    print(*ans, sep="")
