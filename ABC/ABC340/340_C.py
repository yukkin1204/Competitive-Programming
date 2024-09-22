from functools import cache
N=int(input())

@cache
def f(n):
    if n == 1:
        return 0
    else:
        return f(n // 2) + f((n + 1) // 2) + n

print(f(N))
