# D - Match or Not
S = list(input())
T = list(input())
n = len(T)

# Sの前方とTの前方が何文字まで一致するか
count1 = 0
for i in range(n):
    if S[i] == T[i] or S[i] == "?" or T[i] == "?":
        count1 += 1
    else:
        break

# Sの後方とTの後方が何文字まで一致するか
count2 = 0
for i in range(n):
    if S[- 1 - i] == T[- 1 - i] or S[- 1 - i] == "?" or T[- 1 - i] == "?":
        count2 += 1
    else:
        break

for i in range(n + 1):
    # 前方i文字と後方n-i文字が一致しているか
    if count2 >= n - i and count1 >= i:
        print("Yes")
    else:
        print("No")
