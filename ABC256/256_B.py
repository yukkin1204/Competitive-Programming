# Batters
# lにコマの座標を入れる。マス4以降も取り除かれず進むものと考えると解きやすい。
N = int(input())
A = list(map(int, input().split()))

count = 0
l = []

for i in range(N):
    l.append(0)
    l = list(map(lambda x: x + A[i], l))

for num in l:
    if num >= 4:
        count += 1

print(count)


