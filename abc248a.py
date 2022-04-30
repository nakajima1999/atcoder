# ユニークビジョンプログラミングコンテスト2022（AtCoder Beginner Contest 248）
# A - Lacked Number
s = input()
a = set([int(e) for e in s])
b = set([i for i in range(10)])
ans = list(b - a)[0]
print(ans)