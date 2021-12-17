# AtCoder Beginner Contest 216
# A - Signed Difficulty
s = input()
x = s.split('.')[0]
y = s.split('.')[1]
if int(y) <= 2:
    print('{}-'.format(x))
elif int(y) <= 6:
    print(x)
else:
    print('{}+'.format(x))