S = input()
T = input()

a = S.find(T[0].lower())
b = S.find(T[1].lower(), a + 1)
c = S.find(T[2].lower(), b + 1)

if a != -1 and b != -1 and (c != -1 or T[2] == "X"):
    print("Yes")
else:
    print("No")