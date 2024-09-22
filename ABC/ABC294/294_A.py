N = int(input())
A = list(map(int, input().split()))

ans = [num for num in A if num % 2 == 0]
print(*ans)
