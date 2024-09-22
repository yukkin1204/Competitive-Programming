# B - chess960
S = input()

x, y = S.find('B'), S.rfind('B')
a, b = S.find('R'), S.rfind('R')
c = S.find('K')

if (x + y) % 2 == 1 and a < c < b:
    print("Yes")
else:
    print("No")
