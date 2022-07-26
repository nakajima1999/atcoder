# パナソニックグループプログラミングコンテスト2022（AtCoder Beginner Contest 251）
# B - At Most 3 (Judge ver.) 
import itertools
n, w = map(int, input().split())
a = list(map(int, input().split()))

set_n = set()
for i in range(min(3, len(a))):
    for pair in itertools.combinations(a, i + 1):
        total = sum(pair)
        if total <= w:
            set_n.add(total)

ans = len(set_n)
print(ans)