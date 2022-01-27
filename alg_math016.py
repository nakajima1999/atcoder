# アルゴリズムと数学 演習問題集
# 015 - Greatest Common Divisor
import math
from functools import reduce
n = int(input())
a = list(map(int, input().split()))
print(reduce(math.gcd, a))