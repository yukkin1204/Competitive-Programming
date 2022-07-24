# A Unique Letter
S = list(input())

ans = -1

if S[0] != S[1] and S[0] != S[2]:
    ans = S[0]
elif S[1] != S[0] and S[1] != S[2]:
    ans = S[1]
elif S[2] != S[0] and S[2] != S[1]:
    ans = S[2]

print(ans)
