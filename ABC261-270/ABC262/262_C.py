# Min Max Pair
N = int(input())
A = list(map(int, input().split()))
B =[n - 1 for n in A]

count_1 = 0 # インデックスと数字が一致しているものの個数をカウント
count_2 = 0 # インデックスと数字がクロスしているペアの個数をカウント

for i in range(N):
    if B[i] == i:
        count_1 += 1
    elif B[i] > i and B[B[i]] == i:
        count_2 += 1

print(count_1 * (count_1 - 1) // 2 + count_2)
