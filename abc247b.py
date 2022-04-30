# AtCoder Beginner Contest 247
# B - Unique Nicknames
import collections
n = int(input())
a = set()
list_s = []
list_t = []
for i in range(n):
    s, t = map(str, input().split())
    list_s.append(s)
    list_t.append(t)

cout_s = collections.Counter(list_s)
cout_t = collections.Counter(list_t)
ans = 'Yes'
for i in range(n):
    s = list_s[i]
    t = list_t[i]
    if cout_s[s] == 1 and  cout_t[s] == 0:
        next
    elif cout_t[t] == 1 and  cout_s[t] == 0:
        next
    elif s == t:
        next
    else:
        ans = 'No'
print(ans)