# AtCoder Beginner Contest 221
# B - typo
s = input()
t = input()
ans = 'No'
if s == t:
    ans = 'Yes'
else:
    for i in range(len(s) - 1):
        s2 = s[:i] +  s[i + 1] + s[i] + s[i + 2:]
        if s2 == t:
            ans = 'Yes'
            break
print(ans)