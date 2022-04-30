# AtCoder Beginner Contest 245
# A - Good morning
a, b, c, d = map(int, input().split())
if a < c:
    print('Takahashi')
elif a > c:
    print('Aoki')
elif b <= d:
    print('Takahashi')
else:
    print('Aoki')