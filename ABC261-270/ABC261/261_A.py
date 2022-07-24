# Intersection
# 基礎問題
L1, R1, L2, R2 = map(int, input().split())

if L1 <= L2:
    print(max(min(R1, R2) - L2, 0))
else:
    print(max(min(R1, R2) - L1, 0))