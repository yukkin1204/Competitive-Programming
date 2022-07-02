# When?
# 基礎問題
N = int(input())
q = N // 60
r = N % 60

if r < 10:
    print(f"{21 + q}:0{r}")
else:
    print(f"{21 + q}:{r}")

