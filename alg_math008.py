# アルゴリズムと数学 演習問題集
# 008 - Brute Force 1
n, s = map(int, input().split())
if 2 * n <= s:
    ans = n * n
elif n + 1 >= s:
    ans = (s - 1) * s // 2
else:
    m = s - n
    ans = n * m + (n - 1) * n // 2 - (m - 1) * m // 2
print(ans)