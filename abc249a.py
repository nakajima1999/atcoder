# モノグサプログラミングコンテスト2022（AtCoder Beginner Contest 249）
# A - Jogging
def dis(a, b, c, x):
    if a >= x:
        dist = x * b
    elif a + c >= x:
        dist = a * b
    else:
        p = x // (a + c)
        q = x % (a + c)
        dist = b * (a * p +  min(q, a))
    return dist

a, b, c, d, e, f, x = map(int, input().split())
takahashi = dis(a, b, c, x)
aoki = dis(d, e, f, x)
if takahashi > aoki:
    print('Takahashi')
elif takahashi < aoki:
    print('Aoki')
else:
    print('Draw')