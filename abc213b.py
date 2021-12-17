# AtCoder Beginner Contest 213
# B - Booby Prize
import numpy as np
n = int(input())
a = np.array(list(map(int, input().split())))
b = np.argsort(a)
ans = b[-2] + 1
print(ans)
