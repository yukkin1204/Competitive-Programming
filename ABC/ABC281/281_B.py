import re
S = input()

if re.search(r'^[A-Z][1-9][0-9]{5}[A-Z]', S):
    print("Yes")
else:
    print("No")
