# AtCoder Beginner Contest 226
# B - Counting Arrays
n = int(input())
set_a = set()
for i in range(n):
    lst = list(map(str, input().split()))
    l = int(lst[0])
    arr = lst[1:]
    a = '-'.join(arr)
    set_a.add(a)
ans = len(set_a)
print(ans)
