# AtCoder Beginner Contest 236
# B - Who is missing?
import collections
n = int(input())
a = list(map(int, input().split()))
c = collections.Counter(a)
c_sorted = sorted(c.items(), key=lambda x:x[1])
ans = c_sorted[0][0]
print(ans)