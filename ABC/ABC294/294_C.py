N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

C = sorted(A + B)
get_index = {num: i + 1 for i, num in enumerate(C)}

index_A = [get_index[a] for a in A]
index_B = [get_index[b] for b in B]

print(*index_A)
print(*index_B)
