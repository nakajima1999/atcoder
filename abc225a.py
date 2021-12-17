# UNICORNプログラミングコンテスト2021(AtCoder Beginner Contest 225)
# A - Distinct Strings
s = input()
set_s = set([s[0], s[1], s[2]])
if len(set_s) == 1:
    print(1)
elif len(set_s) == 2:
    print(3)
else:
    print(6)