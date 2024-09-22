# C - Four Variables
N = int(input())

# 約数の個数を求める関数
def countDivisor(n):
    count = 0
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            if i * i < n:
                count += 2
            else:
                count += 1
    return count

l = [countDivisor(n) for n in range(1, N)]

ans = 0
for i in range(1, N):
    ans += l[i - 1] * l[N - i - 1]

print(ans)
