# HHKB プログラミングコンテスト 2022（AtCoder Beginner Contest 235）
# 	B - Climbing Takahashi
n = int(input())
h = list(map(int, input().split()))
ans = h[0]
for i in range(1, n):
    if ans < h[i]:
        ans = h[i]
    else:
        break
print(ans) 