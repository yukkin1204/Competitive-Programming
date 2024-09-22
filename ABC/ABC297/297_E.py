# import math
# n, k = map(int, input().split())
# A = list(map(int, input().split()))

# l = math.lcm(A)
# print(l)


# prices.sort()

# # 合計金額をキーに、個数を値に持つ辞書を作成
# total_dict = {}
# for i in range(n):
#     for j in range(1, k+1):
#         total = prices[i] * j
#         if total not in total_dict:
#             total_dict[total] = 1

# # 辞書のキー（合計金額）を昇順にソートして、k番目の要素を出力
# sorted_totals = sorted(list(total_dict.keys()))
# print(sorted_totals[k-1])

n, k = map(int, input().split())
prices = list(map(int, input().split()))
prices.sort()

# 合計金額をキーに、個数を値に持つ辞書を作成
total_dict = {}
for i in range(n):
    for j in range(1, k+1):
        total = prices[i] * j
        if total not in total_dict:
            total_dict[total] = 1
        else:
            total_dict[total] += 1

# 辞書のキー（合計金額）を昇順にソートして、k番目の要素を出力
sorted_totals = sorted(list(total_dict.keys()))
print(sorted_totals[k-1])
