# アルゴリズムと数学 演習問題集
# 025 - Jiro's Vacation
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
ans = (sum(a) + sum(b) * 2) / 3
print(ans)