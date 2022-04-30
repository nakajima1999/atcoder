# AtCoder Beginner Contest 240
# A - Edge Checker
a, b = map(int, input().split())
if b - a == 1:
    print('Yes')
elif a == 1 and b == 10:
    print('Yes')
else:
    print('No')