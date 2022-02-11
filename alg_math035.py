# アルゴリズムと数学 演習問題集
# 035 - Two Circles
import math
x1, y1, r1 = map(int, input().split())
x2, y2, r2 = map(int, input().split())

d = math.sqrt(((y1 - y2) ** 2) + ((x1 - x2) ** 2))
if r1 + r2 < d:  # 2つの円の内部に共通部分は存在せず、2つの円は接していない
    ans = 5
elif r1 + r2 == d:  # 2つの円の内部に共通部分は存在しないが、2つの円は接している
    ans = 4
elif abs(r1 - r2) < d < r1 + r2:  # 2つの円が互いに交差する
    ans = 3
else:
    if r1 < r2:
        r1, r2 = r2, r1
    if d == r1 - r2:  # 一方の円が他方の円を完全に含み、2つの円は接している
        ans = 2
    else:
        ans = 1  # 一方の円が他方の円を完全に含み、2つの円は接していない
print(ans)