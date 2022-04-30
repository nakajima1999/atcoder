# AtCoder Beginner Contest 242
# A - T-shirt
a, b, c, x = map(int, input().split())
if x <= a:
    ans = 1
elif x > b:
    ans = 0
else:
    ans = c / (b - a)
print(ans)