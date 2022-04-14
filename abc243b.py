# AtCoder Beginner Contest 243
# B - Hit and Blow
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
set_a = set(a)
set_b = set(b)
x = 0
y = 0
for i in range(n):
    if a[i] == b[i]:
        x += 1
    elif a[i] in set_b:
        y += 1
print(x)
print(y)