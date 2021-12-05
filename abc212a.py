a, b = map(int, input().split())
if 0 < a and b == 0:
    ans = 'Gold'
elif a == 0 and 0 < b:
    ans = 'Silver'
else:
    ans = 'Alloy'
print(ans)