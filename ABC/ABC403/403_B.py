import string

T = input()
U = input()

for char1 in string.ascii_lowercase:
    for char2 in string.ascii_lowercase:
        for char3 in string.ascii_lowercase:
            for char4 in string.ascii_lowercase:
                new_T = T.replace("?", char1, 1).replace("?", char2, 1).replace("?", char3, 1).replace("?", char4, 1)
                if U in new_T:
                    print("Yes")
                    exit()

print("No")
