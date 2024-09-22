# Batters
# マスの状態をlistで管理する自然な解法
N = int(input())
A = list(map(int, input().split()))

count = 0
l = [0, 0, 0, 0]

for num in A:
    m = [0, 0, 0, 0]
    l[0] = 1
    for i in range(4):
        if l[i] == 1:
            if i + num >= 4:
                count += 1
            else:
                m[i + num] = 1
    l = m

print(count)
