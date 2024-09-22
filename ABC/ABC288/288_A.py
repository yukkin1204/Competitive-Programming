# A - Many A+B Problems
from sys import stdin
N = int(input())
l = [list(map(int, stdin.readline().split())) for _ in range(N)]

for nums in l:
    print(nums[0] + nums[1])

