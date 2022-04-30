# モノグサプログラミングコンテスト2022（AtCoder Beginner Contest 249）
# 	B - Perfect String
s = input()
t = [e for e in s]
t.sort()
if len(t) != len(set(t)) or s == s.upper() or  s == s.lower():
    print('No')
else:
    print('Yes')
