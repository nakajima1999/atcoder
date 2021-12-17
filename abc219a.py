# サイシードプログラミングコンテスト2021（AtCoder Beginner Contest 219）
#  A - AtCoder Quiz 2
x = int(input())
if x < 40:
    print(40 - x)
elif x < 70:
    print(70 - x)
elif x < 90:
    print(90 - x)
else:
    print('expert')