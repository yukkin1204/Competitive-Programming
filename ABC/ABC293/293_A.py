# A - Swap Odd and Even
S = input()

ans = ""
for i in range(len(S) // 2):
    ans += S[2 * i + 1]
    ans += S[2 * i]

print(ans)
