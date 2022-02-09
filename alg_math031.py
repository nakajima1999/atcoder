# アルゴリズムと数学 演習問題集
# 031 - Taro's Vacation
n = int(input())
a = list(map(int, input().split()))
# dp[i][j]: i日目に宿題をしない/して(0/1)，実力を最大にする場合の実力
dp = [[0] * 2 for i in range(n + 1)]
for i in range(n):
    dp[i + 1][0] = max(dp[i][0], dp[i][1])  # i + 1日目に宿題をしない場合，i日目の実力
    dp[i + 1][1] = dp[i][0] + a[i]  # i + 1日目に宿題をする場合，i日目に宿題をしない場合の実力にa[i]を加算した実力
ans = max(dp[n])
print(ans)