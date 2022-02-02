# アルゴリズムと数学 演習問題集
# 020 - Choose Cards 2
'''
# Python (3.8.2)/ 2412 ms / AC
n = int(input())
arr = list(map(int, input().split()))
ans = 0
for a in range(n - 4):
    for b in range(a + 1, n - 3):
        for c in range(b + 1, n - 2):
            for d in range(c + 1, n - 1):
                x = arr[a]+arr[b]+arr[c]+arr[d]
                y = 1000 - x
                arr_2 = arr[d + 1:]
                if y in arr_2:
                   ans += arr_2.count(y)
print(ans)
'''

'''
# Python (3.8.2) / 5513 ms / TLE
# PyPy3 (7.3.0) / 431 ms / AC
n = int(input())
arr = list(map(int, input().split()))
ans = 0
for a in range(n - 4):
    for b in range(a + 1, n - 3):
        for c in range(b + 1, n - 2):
            for d in range(c + 1, n - 1):
                for e in range(d + 1, n):
                    if arr[a] + arr[b] + arr[c] + arr[d] + arr[e] == 1000:
                        ans += 1
print(ans)
'''

# Python (3.8.2) / 74 ms / AC
n = int(input())
arr = list(map(int, input().split()))
# dp[i][j]: i枚を使って合計jを作ることができるパターン数
dp = [[0 for i in range(1001)] for j in range(6)]
dp[0][0] = 1
for a in arr:
    for i in range(5, 0, -1):
        for j in range(1000, a - 1, -1):
            # iより1枚少ない枚数(i - 1)でjよりもa少ない合計(j-a)にできるパターン数を加算
            dp[i][j] += dp[i - 1][j - a]  
ans = dp[5][1000]
print(ans)