# AtCoder Beginner Contest 221
# A - Seismic magnitude scales
a, b = map(int, input().split())
ans = 32 ** (a - b)
print(ans)