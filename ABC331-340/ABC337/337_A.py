from sys import stdin
N = int(input())
l = [list(map(int, stdin.readline().split())) for _ in range(N)]

sum_X = 0
sum_Y = 0

for pair in l:
    sum_X += pair[0]
    sum_Y += pair[1]

if sum_X > sum_Y:
    print("Takahashi")
elif sum_X < sum_Y:
    print("Aoki")
else:
    print("Draw")