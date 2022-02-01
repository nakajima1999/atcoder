# アルゴリズムと数学 演習問題集
# 018 - Convenience Store 1
import collections
n = int(input())
a = list(map(int, input().split()))
c = collections.Counter(a)
ans = c[100] * c[400] + c[200] * c[300]
print(ans)