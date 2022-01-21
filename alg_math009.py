# アルゴリズムと数学 演習問題集
# 009 - Brute Force 2
n, s = map(int, input().split())
a = list(map(int, input().split()))
# 動的計画法: 部分話問題
# dp[i][j]: i番目までの整数の中からいくつか選んで総和をjとすることが可能かどうか(0/1)
dp = [[0 for i in range(s + 1)] for j in range(n + 1)]  
dp[0][0] = 1
for i in range(n):
    for j in range(s + 1):
        if a[i] <= j:
            if dp[i][j - a[i]] == 1:
                dp[i + 1][j] = 1
            else:
                dp[i + 1][j] = dp[i][j]
        else:
            dp[i + 1][j] = dp[i][j]
ans = dp[n][s]
if ans == 1:
    print('Yes')
else:
    print('No')