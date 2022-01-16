# アルゴリズムと数学 演習問題集
# 007 - Number of Multiples 1
import math
def my_lcm(x, y):
    return (x * y) // math.gcd(x, y)
n, x, y = map(int, input().split())
a = n // x
b = n // y
c = n // my_lcm(x, y)
ans = a + b - c
print(ans)