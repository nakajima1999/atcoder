# AtCoder Beginner Contest 210
# B - Bouzu Mekuri
n = int(input())
s = input()
k = s.index('1')
if k % 2 == 0:
    print('Takahashi')
else:
    print('Aoki')