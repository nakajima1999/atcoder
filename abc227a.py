# キーエンスプログラミングコンテスト2021-Nov. (AtCoder Beginner Contest 227)
# A - Last Card
n, k, a = map(int, input().split())
k -= n - a + 1
ans = k % n
if ans == 0:
    ans = n
print(ans)