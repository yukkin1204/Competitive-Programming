# Perfect String
S = input()

A = set()
flg_a = False
flg_b = False
flg_c = True

for char in S:
    if char.isupper():
        flg_a = True
    if char.islower():
        flg_b = True
    if char not in A:
        A.add(char)
    else:
        flg_c = False

if flg_a and flg_b and flg_c:
    print("Yes")
else:
    print("No")