n, k = map(int, input().split())
c = list(map(int, input().split()))
candy = c[:k]
arr_ans = []
k = len(set(candy))
arr_ans.append(k)
for i in range(k, n):
    rm_candy = candy[0]
    add_candy = c[i]
    if rm_candy == add_candy:
        next
    else:
        if candy.count(rm_candy) == 1:
            k -= 1
        if candy.count(add_candy) == 0:
            k += 1

        arr_ans.append(k)
        candy = candy[1:] + [c[i]]
        
ans = max(arr_ans)
print(ans)