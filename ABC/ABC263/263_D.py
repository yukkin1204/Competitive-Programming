# Left Right Operation
N, L, R = map(int, input().split())
A = list(map(int, input().split()))

# Lのゾーン|Aのゾーン|Mのゾーン
# 2つの区切り線をどこにするべきか考える問題
# 右の区切り線を1つずつ右にずらすことを考える
# そのとき左の区切り線の場所は、ずらす前の場所から動かないか、右の区切り線と同じ場所になるかの2択

ans = R * N
ac_a = 0 # 左からi項のAの和
ac_b = 0 # 左からi項の(A-L)の和、つまりAをLに置き換えた場合のお得度
mx = 0 # ac_bの暫定max
for i, a in enumerate(A):
    ac_a += a
    ac_b += (a - L)
    mx = max(mx, ac_b)
    # (ac_a - mx)が右の区切り線を位置iで固定したときのLのゾーンとAのソーンの和の最小値
    now = ac_a - mx + R * (N - i - 1)
    ans = min(ans, now)
print(ans)
