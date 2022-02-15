# パナソニックプログラミングコンテスト2021(AtCoder Beginner Contest 231)
# B - Election
from collections import defaultdict
d = defaultdict(int)
n = int(input())
for i in range(n):
    s = input()
    d[s] += 1
d_sorted = sorted(d.items(), key=lambda x:x[1], reverse=True)
ans = d_sorted[0][0]
print(ans)