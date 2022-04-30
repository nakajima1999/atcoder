# AtCoder Beginner Contest 234
# B - Longest Segment
import math
def dist(a, b, c, d):
    dis = math.sqrt((a - c) ** 2 + (b - d) ** 2)
    return dis

n = int(input())
xy = []
for i in range(n):
    x, y = map(int, input().split())
    xy.append((x, y))

ans = 0
for i in range(n - 1):
    a, b = xy[i]
    for j in range(i + 1, n):
        c, d = xy[j]
        dis = dist(a, b, c, d)
        ans = max(ans, dis)
print(ans)