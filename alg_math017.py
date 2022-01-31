# アルゴリズムと数学 演習問題集
# 017 - Least Common Multiple of N Integers
import math
from functools import reduce
def lcm(a, b):
    return a * b // math.gcd(a, b)
n = int(input())
a = list(map(int, input().split()))
print(reduce(lcm, a))