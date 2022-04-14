# M-SOLUTIONS プロコンオープン2021(AtCoder Beginner Contest 232)
# B - Caesar Cipher
s = input()
t = input()
k = (ord(t[0]) - ord(s[0]) + 26) % 26
ans = 'Yes'
for i in range(len(s)):
    if (ord(t[i]) - ord(s[i]) + 26) % 26 != k:
        ans = 'No'
        break
print(ans)