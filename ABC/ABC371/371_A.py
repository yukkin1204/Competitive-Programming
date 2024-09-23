S_AB, S_AC, S_BC = input().split()

if (S_AB == "<" and S_AC == ">") or (S_AB == ">" and S_AC == "<"):
  print("A")
elif (S_AB == "<" and S_BC == "<") or (S_AB == ">" and S_BC == ">"):
  print("B")
else:
  print("C")
