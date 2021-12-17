# AtCoder Beginner Contest 216
# B - Same Name
n = int(input())
set_names = set()
for i in range(n):
    st_name = input()
    set_names.add(st_name)

if len(set_names) == n:
    print('No')
else:
    print('Yes')