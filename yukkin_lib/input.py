# 1行1列受け
#str型で受け取るとき
s = input()
#int型で受け取るとき
s = int(input())

# 1行2列受け
#str型で受け取るとき
s, t = input().split()
# int型
s, t = map(int, input().split())

# 1行n列受け
# str型
l = input().split()
# int型
l = list(map(int, input().split()))

# n行2列受け
# int型([xi,yi]として格納)
N = int(input())
l = [list(map(int, input().split())) for l in range(N)]

