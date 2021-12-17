# AtCoder Beginner Contest 218
# B - qwerty
p = list(map(int, input().split()))
s = [chr(p[i] + 96)  for i in range(len(p))]
ans = ''.join(s)
print(ans)