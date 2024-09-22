N = int(input())

if 1 <= N <= 99:
    print(100 - N)
elif 100 <= N <= 199:
    print(200 - N)
else:
    print(300 - N)