# N進数
l = list(input())

N = len(l)
ans = 0
for i in range(N):
    ans += int(l[i]) * (2 ** (N - 1 - i))
print(ans)
