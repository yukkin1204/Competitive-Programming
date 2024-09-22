# D - Step Up Robot
N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = set(map(int, input().split()))
X = int(input())

# 登れる段を管理
S = {0}

for i in range(X + 1):
    if i in S:
        for num in A:
            if i + num not in B:
                S.add(i + num)

if X in S:
    print("Yes")
else:
    print("No")
