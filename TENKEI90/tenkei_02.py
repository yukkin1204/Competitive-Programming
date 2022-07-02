# Encyclopedia of Parentheses
# bit全探索
# iを2進数表記した場合の下から数えてn桁目（一番下の桁を 0 とする）が
# 1であるかどうかをチェックするためのコードは、(i >> n) & 1
N = int(input())

for i in range(2 ** N):
    s = ""
    dep = 0
    for j in range(N):
        if dep < 0:
            break
        if (i >> N - 1 - j) & 1:
            s += ")"
            dep -= 1
        else:
            s += "("
            dep += 1
    if dep == 0:
        print(s)

