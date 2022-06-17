# Last Two Digits
N = int(input())

r = N % 100
if r < 10:
    print(f"0{r}")
else:
    print(r)

