# アルゴリズムと数学 演習問題集
# 024 - Answer Exam Randomly
ans = 0
n = int(input())
for i in range(n):
    p, q = map(int, input().split())
    ans += q / p
print(ans)