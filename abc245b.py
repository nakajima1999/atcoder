# AtCoder Beginner Contest 245
# B - Mex
n = int(input())
a = set(list(map(int, input().split())))
b = set([i for i in range(20001)])
c = b - a
ans = min(c)
print(ans)