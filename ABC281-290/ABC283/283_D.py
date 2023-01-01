# D - Scope
# 愚直な解法
# 全体の文字管理と括弧内の文字管理の連動がミソ
S = input()
s = set() # 全体の文字管理
q = [set()] # 括弧内の文字管理

for char in S:
    if char == '(':
        # qに最新setを作成
        q.append(set())
    elif char == ')':
        # qの最新setの文字をsから削除し、最新setも削除
        for j in q[-1]:
            s.remove(j)
        q.pop()
    else:
        # sに今回の文字がなければ、その文字をqの最新setとsに追加
        if char in s:
            print("No")
            exit()
        else:
            q[-1].add(char)
            s.add(char)

print("Yes")
