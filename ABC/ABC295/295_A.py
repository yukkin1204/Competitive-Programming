N = int(input())
W = input().split()

for word in W:
    if word in {"and", "not", "that", "the", "you"}:
        print("Yes")
        exit()
print("No")