N = int(input())
H = list(map(int, input().split()))

ans = [0]
stack = []

# 後方から考える
for i in range(N - 2, -1, -1):
    # ビルi+1より低いビルをstackから除去
    while stack and H[i + 1] > stack[-1]:
        stack.pop()
    # ビルi+1をstackに追加
    stack.append(H[i + 1])
    # ビルiから見た答え
    ans.append(len(stack))

ans = ans[::-1]
print(*ans)