# AtCoder Beginner Contest 237
# B - Matrix Transposition
import numpy as np
h, w = map(int, input().split())
a = [list(map(int, input().split())) for i in range(h)]
a = np.array(a)
b = a.T.tolist()
for c in b:
    c = [str(e) for e in c]
    print(' '.join(c))
