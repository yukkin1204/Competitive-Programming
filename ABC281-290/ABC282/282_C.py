N = int(input())
S = list(input())
flg = False

for i in range(N):
    if S[i] == '"':
        flg = not flg
    elif S[i] == ',' and not flg:
        S[i] = '.'

print(*S, sep='')
