# B - Qual B
N, K = map(int, input().split())
S = input()

ans = ""
count = 0

for char in S:
    if char == "o" and count < K:
        ans += "o"
        count += 1
    else:
        ans += "x"

print(ans)
