# アルゴリズムと数学 演習問題集
# 030 - Knapsack 1
N,W = map(int,input().split())
w = []
v = []
for i in range(N):
    x,y = map(int,input().split())
    w.append(x)
    v.append(y)

dp = [[0]*(W+1) for j in range(N+1)] # DPテーブルの作成

for i in range(N):
    for j in range(W + 1):
        if j < w[i]: # 選ばない時
            dp[i + 1][j] = dp[i][j]
        else: # 選ぶ時
            dp[i + 1][j] = max(dp[i][j],dp[i][j - w[i]] + v[i])
ans = dp[N][W]
print(ans)

'''
メモ
Python(3.8.2) / TLE / 2214ms
PyPy3(7.3.0) /  AC / 243ms
'''