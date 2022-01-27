# アルゴリズムと数学 演習問題集
# 015 - Greatest Common Divisor
import math
from functools import reduce
n = int(input())
a = list(map(int, input().split()))
print(reduce(math.gcd, a))

'''
メモ
- functools モジュール: 高階関数
    - 関数に影響を及ぼしたり，他の関数を返したりする関数のためのもの
- functools.reduce(function, iterable[, initializer])
    - iterable の要素に対して、iterable を単一の値に短縮するような形で 
      2 つの引数をもつ function を左から右に累積的に適用
'''