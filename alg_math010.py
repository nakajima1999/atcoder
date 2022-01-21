# アルゴリズムと数学 演習問題集
# 010 - Factorial
n = int(input())
ans = 1
for i in range(n):
    ans *= i + 1
print(ans)