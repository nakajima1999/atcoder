# ユニークビジョンプログラミングコンテスト2022（AtCoder Beginner Contest 248）
# B - Slimes
a, b, k = map(int, input().split())
ans = 0
while a < b:
    a *= k
    ans += 1
print(ans)