n = int(input())
ans = 'Yes'
node = set()
for i in range(n - 1):
    a, b = map(int, input().split())
    if i == 0:
        star = [a, b]
        node.add(a)
        node.add(b)
    elif i == 1:
        if a in star and b in star:
            ans = 'No'
        elif a in star:
            star = a
            node.add(b)
        elif b in star:
            star = b
            node.add(a)
    else:
        if a == star:
            node.add(b)
        elif b == star:
            node.add(a)
        else:
            ans = 'No'
if len(node) != n:
    ans = 'No'
print(ans)