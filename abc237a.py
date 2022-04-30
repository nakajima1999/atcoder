# AtCoder Beginner Contest 237
# A - Not Overflow
n = int(input())
if -(2 ** 31) <= n < 2 ** 31:
    print('Yes')
else:
    print('No')