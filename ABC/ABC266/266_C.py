# C - Convex Quadrilateral
# 頂点をA→B→C→D→Aと辿るとき、その道のりが常に反時計回りかを調べればよい。
# A→B→Cの道のりが反時計回りのとき、vec_abとvec_bcの外積が正となることを利用する。
from sys import stdin
l = [list(map(int, stdin.readline().split())) for _ in range(4)]

# 2ベクトルの外積を計算
def cross(vec1, vec2):
    return vec1[0] * vec2[1] - vec1[1] * vec2[0]

vec_ab = [l[0][0]-l[1][0], l[0][1]-l[1][1]]
vec_bc = [l[1][0]-l[2][0], l[1][1]-l[2][1]]
vec_cd = [l[2][0]-l[3][0], l[2][1]-l[3][1]]
vec_da = [l[3][0]-l[0][0], l[3][1]-l[0][1]]

if cross(vec_ab, vec_bc) > 0 and cross(vec_bc, vec_cd) > 0 and cross(vec_cd, vec_da) > 0 and cross(vec_da, vec_ab) > 0:
    print("Yes")
else:
    print("No")
