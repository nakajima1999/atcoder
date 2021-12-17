# AtCoder Beginner Contest 217
# B - AtCoder Quiz
s = set([input() for i in range(3)])
atcoder = set(['ABC', 'ARC', 'AGC', 'AHC'])
ans = list(atcoder - s)[0]
print(ans)