# アルゴリズムと数学 演習問題集
# 029 - Climb Stairs
n = int(input())
if n == 1:
    ans = 1
elif n == 2:
    ans = 2
else:
    a = [0 for i in range(n + 1)]
    a[1] = 1
    a[2] = 2
    for i in range(3, n + 1):
        a[i] = a[i - 1] + a[i - 2]
    ans = a[n]
print(ans)