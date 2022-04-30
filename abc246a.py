# AtCoder Beginner Contest 246
# 	A - Four Points
from collections import defaultdict
d_x = defaultdict(int)
d_y = defaultdict(int)
for i in range(3):
    x, y = map(int, input().split())
    d_x[x] += 1
    d_y[y] += 1
dx_sorted = sorted(d_x.items(), key=lambda x:x[1])
dy_sorted = sorted(d_y.items(), key=lambda x:x[1])
x = dx_sorted[0][0]
y = dy_sorted[0][0]
print(x, y)