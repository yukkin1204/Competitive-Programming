# Full House
# ソートすることで、確認パターンを10から2に減らせる
l = list(map(int, input().split()))
l.sort()

if (l[0] == l[1] == l[2] and l[3] == l[4]) or (l[0] == l[1] and l[2] == l[3] == l[4]):
    print("Yes")
else:
    print("No")
