# トヨタシステムズプログラミングコンテスト2021(AtCoder Beginner Contest 228)
# B - Takahashi's Secret
n, x = map(int, input().split())
a = list(map(int, input().split()))
b = set()
b.add(x)
for i in range(n):
    f = a[x - 1]
    if f not in b:
        b.add(f)
        x = f
    else:
        break
ans = len(b)
print(ans)