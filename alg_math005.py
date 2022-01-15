# アルゴリズムと数学 演習問題集
# 005 - Modulo 100
n = int(input())
a = list(map(int, input().split()))
ans = sum(a) % 100
print(ans)