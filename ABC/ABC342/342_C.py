import string
N = int(input())
S = input()
Q = int(input())

alphabet = string.ascii_lowercase
goal = string.ascii_lowercase

for i in range(Q):
    c, d = map(str, input().split())
    goal = goal.replace(c, d)

translation = str.maketrans(alphabet, goal)

S = S.translate(translation)
print(S)