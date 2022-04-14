# AtCoder Beginner Contest 243
# A - Shampoo
v, a, b, c = map(int, input().split())
m = a + b + c
p = v // m
v -= m * p
if v < a:
    print('F')
else:
    v -= a
    if v < b:
        print('M')
    else:
        print('T')
