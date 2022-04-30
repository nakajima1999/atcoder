# モノグサプログラミングコンテスト2022（AtCoder Beginner Contest 238）
# A - Exponential or Quadratic
import math
n = int(input())
if n > 2 * math.log(n, 2):
    print('Yes')
else:
    print('No')