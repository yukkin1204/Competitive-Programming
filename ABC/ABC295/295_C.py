N = int(input())
A = list(map(int, input().split()))

d = dict()
for num in A:
    d[num] = d.get(num, 0) + 1

ans = 0
for val in d.values():
    ans += val // 2

print(ans)