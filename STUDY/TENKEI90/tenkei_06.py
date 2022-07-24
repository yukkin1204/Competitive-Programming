# Smallest Subsequence
# 辞書順最小は前から貪欲法
# 貪欲法
# 適当な基準を用いて、局所的に最適なケースを連続して選択する解法
N, K = map(int, input().split())
S = input()

count = 0
stack = []
for char in S:
    while stack and count < N - K and stack[-1] > char:
        stack.pop()
        count += 1
    stack.append(char)

print(''.join(stack[0:K]))

# 8行目から12行目で行っていること
# kittyonyourlap(14文字)の5文字部分列の場合
# kを追加 stack=[k], count=0
# iを追加 stack=[i], count=1 kiよりiの方が良いためkは除外する
# tを追加 stack=[i,t], count=1
# tを追加 stack=[i,t,t], count=1
# yを追加 stack=[i,t,t,y], count=1
# oを追加 stack=[i,o], count=4
# nを追加 stack=[i,n], count=5
# yを追加 stack=[i,n,y], count=5
# oを追加 stack=[i,n,o], count=6
# uを追加 stack=[i,n,o,u], count=6
# rを追加 stack=[i,n,o,r], count=7
# lを追加 stack=[i,n,l], count=9 除外文字数が9に達したことからnは除外できない
# aを追加 stack=[i,n,l,a], count=9
# pを追加 stack=[i,n,l,a,p], count=9
