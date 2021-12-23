h, w = map(int, input().split())
arr = []
for i in range(h):
    a = list(map(int, input().split()))
    arr.append(a)

ans = 'Yes'
for i1 in range(h - 1):
    for i2 in range(i1 + 1, h):
        for j1 in range(w - 1):
            for j2 in range(j1 + 1, w):
                if arr[i1][j1] + arr[i2][j2] <= arr[i2][j1] + arr[i1][j2]:
                    next
                else:
                    ans = 'No'
                    break
print(ans)