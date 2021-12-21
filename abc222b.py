# エクサウィザーズプログラミングコンテスト2021（AtCoder Beginner Contest 222）
# 	B - Failing Grade
n, p = map(int, input().split())
a = list(map(int, input().split()))
ans = len([a[i] for i in range(n) if a[i] < p])
print(ans)