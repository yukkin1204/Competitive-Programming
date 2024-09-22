# C - Cash Register
S = list(input())

i = 0
count = 0
while i < len(S):
    count += 1
    # 0が2連続で続く場合の処理 (count1でindexを2つ進める)
    if i != len(S) - 1 and S[i] == "0" and S[i + 1] == "0":
        i += 2
    else:
        i += 1
print(count)
