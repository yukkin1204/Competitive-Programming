N = int(input())
A = list(map(int, input().split()))

def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n ** 0.5 // 1)) + 1):
        if temp % i == 0:
            cnt = 0
            while temp % i == 0:
                cnt += 1
                temp //= i
            arr.append([i, cnt])
    if temp != 1:
        arr.append([temp, 1])
    return arr

def f(a):
    fac = factorization(a)
    res = 1
    for k, n in fac:
        if n % 2:
            res *= k
    return res

d = dict()
ans = 0
zero_count = 0

for num in A:
    if num == 0:
        ans += N - 1 - zero_count
        zero_count += 1
    else:
        s = f(num)
        if s in d:
            d[s] += 1
        else:
            d[s] = 1

for a in d:
    if d[a] >= 2:
        ans += (d[a] * (d[a] - 1)) // 2

print(ans)