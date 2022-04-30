# AtCoder Beginner Contest 241（Sponsored by Panasonic）
# B - Pasta
import collections
n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a_count = collections.Counter(a)
b_count = collections.Counter(b)
ans = 'Yes'
for e in b_count:
    if b_count[e] > a_count[e]:
        ans = 'No'
        break
print(ans)