# トヨタシステムズプログラミングコンテスト2021(AtCoder Beginner Contest 228)
# A - On and Off
s, t, x = map(int, input().split())
if s < t:
    if s <= x < t:
        print('Yes')
    else:
        print('No')
else:
    if s <= x <= 23 or 0 <= x < t:
        print('Yes')
    else:
        print('No')