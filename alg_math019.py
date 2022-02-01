# アルゴリズムと数学 演習問題集
# 018 - Convenience Store 1
import collections
n = int(input())
a = list(map(int, input().split()))
c = collections.Counter(a)
ans = c[1] * (c[1] - 1) // 2 + c[2] * (c[2] - 1) // 2 + c[3] * (c[3] - 1) // 2
print(ans)