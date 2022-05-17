# Poem Online Judge
N = int(input())
l = [list(input().split()) for l in range(N)]

S = set()
max = -1
ans = -1

for i in range(0, N):
    if l[i][0] not in S:
        S.add(l[i][0])
        if int(l[i][1]) > max:
            max = int(l[i][1])
            ans = i + 1
print(ans)