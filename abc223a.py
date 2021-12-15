# AtCoder Beginner Contest 223
# A - Exact Price
x = int(input())
if x % 100 == 0 and x // 100 >= 1:
    print('Yes')
else:
    print('No')