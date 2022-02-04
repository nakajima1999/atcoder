# アルゴリズムと数学 演習問題集
# 022 - Choose Cards 3
import collections
n = int(input())
a = list(map(int, input().split()))
c = collections.Counter(a)
c_sorted = sorted(c.items(), key=lambda x:x[0])
ans = 0
for e in c_sorted:
    f = 100000 - e[0]
    x =  e[1]
    y = c[f]

    if e[0] > 50000:
        break
    elif e[0] == 50000:
        ans += x * (x - 1) // 2
    else:
        ans += x * y
print(ans)