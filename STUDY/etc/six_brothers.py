import itertools

brothers = ["アキラ", "カオル", "サツキ", "タクミ", "ナギサ", "ハルカ"]
# 兄弟の並び順(全720通り)
brother_patterns = set(itertools.permutations(brothers))

sexs = [0, 0, 0, 1, 1, 1]
# 性別の組合せ(全20通り、0が男性、1が女性)
sex_patterns = set(itertools.permutations(sexs))

# 解答保存用list
brother_ans = []
sex_ans = []

# 兄弟check関数
# 「aの兄(姉)ならばbです」
def check(a, b, sex, brother_pattern, sex_pattern):
    # aが何番目に並んでいるかを確認
    index = brother_pattern.index(a)
    # aより前にb以外の兄(姉)がいないかを調べる
    for i in range(index):
        if sex_pattern[i] == sex and brother_pattern[i] != b:
            return False
    return True

# 全探索
for brother_pattern in brother_patterns:
    for sex_pattern in sex_patterns:
        # 問題文の条件を満たすかcheck
        if check("アキラ", "カオル", 0, brother_pattern, sex_pattern) \
            and check("カオル", "サツキ", 0, brother_pattern, sex_pattern) \
            and check("サツキ", "タクミ", 1, brother_pattern, sex_pattern) \
            and check("タクミ", "ナギサ", 1, brother_pattern, sex_pattern) \
            and check("ナギサ", "ハルカ", 0, brother_pattern, sex_pattern):
            # 条件を満たせば、解答保存用listに追加する
            brother_ans.append(brother_pattern)
            sex_ans.append(sex_pattern)

# 解答保存用listの中身を出力
print(brother_ans)
print(sex_ans)
