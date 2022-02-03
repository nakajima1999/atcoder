# アルゴリズムと数学 演習問題集
# 021 - Combination Easy
import math
def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))
n, r = map(int, input().split())
ans = combinations_count(n, r)
print(ans)

'''
メモ
- 階乗: math.factorial()
'''