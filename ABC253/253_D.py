# FizzBuzz Sum Hard
# 集合の基礎問題
import math

N, A, B = map(int, input().split())

q_A = N // A
A_end = A * q_A
q_B = N // B
B_end = B * q_B

C = A * B // math.gcd(A, B) #最小公倍数
q_C = N // C
C_end = C * q_C

sum_N = N * (N + 1) // 2
sum_A = q_A * (A + A_end) // 2
sum_B = q_B * (B + B_end) // 2
sum_C = q_C * (C + C_end) // 2

print(sum_N - (sum_A + sum_B - sum_C))
