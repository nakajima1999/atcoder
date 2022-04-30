# モノグサプログラミングコンテスト2022（AtCoder Beginner Contest 238）
# B - Pizza
n = int(input())
a = list(map(int, input().split()))
b = []
b.append(a[0])
for i in range(1, n):
    b.append((b[-1] + a[i]) % 360)
b.append(0)
b.append(360)
b.sort()

c = []
for i in range(n + 1):
    c.append(b[i + 1] - b[i])
ans = max(c)
print(ans)