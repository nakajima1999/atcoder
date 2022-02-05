# アルゴリズムと数学 演習問題集
# 026 - Coin Gacha
n = int(input())
ans = 0
for i in range(n):
    ans += n / (i + 1)
print(ans)