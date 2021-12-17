# サイシードプログラミングコンテスト2021（AtCoder Beginner Contest 219）
# B - Maritozzo
dic_s = {}
for i in range(3):
    s = input()
    dic_s[str(i + 1)] = s
t = input()
ans = [dic_s[t[i]] for i in range(len(t))]
ans = ''.join(ans)
print(ans)