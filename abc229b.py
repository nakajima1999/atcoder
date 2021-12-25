# NECプログラミングコンテスト2021(AtCoder Beginner Contest 229)
# B - Hard Calculation
a, b = map(str, input().split())
ans = 'Easy'
for i in range(min(len(a), len(b))):
    x = int(a[-(i + 1)])
    y = int(b[-(i + 1)])
    if x + y >= 10:
        ans = 'Hard'
        break
print(ans)