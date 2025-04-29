N = int(input())
S = [input() for _ in range(N)]

is_login = False
count = 0

for row in S:
    if row == "login":
        is_login = True
    elif row == "logout":
        is_login = False
    elif row == "private" and not is_login:
        count += 1

print(count)
