# Adjacent Squares
H, W = map(int, input().split())
R, C = map(int, input().split())


if (R == 1 or R == H) and (C == 1 or C == W):
    ans = 2
elif (1 < R < H and 1 < C < W):
    ans = 4
else:
    ans = 3

if H == 1:
    ans -= 1
if W == 1:
    ans -= 1

print(ans)