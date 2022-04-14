# AtCoder Beginner Contest 233
# A - 10yen Stamp
x, y = map(int, input().split())
if x >= y:
    ans = 0
else:
    ans = (y - x) // 10 + max(0, min(1, (y - x) % 10))
print(ans)