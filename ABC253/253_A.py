# Median?
a, b, c = map(int, input().split())
if ((b - a >= 0 and c - b >= 0) or (b - a <= 0 and c - b <= 0)):
    print("Yes")
else:
    print("No")