# A - flip
s = input()

ans = ""
for char in s:
    if char == "0":
        ans += "1"
    else:
        ans += "0"

print(ans)
