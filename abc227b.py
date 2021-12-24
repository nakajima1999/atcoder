# キーエンスプログラミングコンテスト2021-Nov. (AtCoder Beginner Contest 227)
# B - KEYENCE building
n = int(input())
list_s = list(map(int, input().split()))
ans = 0
for i in range(n):
    s = list_s[i]
    f = 1
    for a in range(1, min(143, s)):
        if (s - 3 * a) != 0 and (s - 3 * a) % (4 * a + 3) == 0:
            f = 0
            break
    ans += f
print(ans)