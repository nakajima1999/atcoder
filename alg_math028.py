# アルゴリズムと数学 演習問題集
# 028 - Frog 1
n = int(input())
h = list(map(int, input().split()))
dp = [0 for i in range(n + 1)]
dp[2] = abs(h[0] - h[1])  # DP
for i in range(3, n + 1):
    a = dp[i - 2] + abs(h[i - 1] - h[i - 3])  # 2つ前からジャンプする場合
    b = dp[i - 1] + abs(h[i - 1] - h[i - 2])  # 1つ前からジャンプする場合
    dp[i] = min(a, b)  # i番目の足場に辿り着くまでのコストが小さい方
ans = dp[-1]
print(ans)