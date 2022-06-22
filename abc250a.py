# AtCoder Beginner Contest 250
# A - Adjacent Squares
def adjacent(x, n, ans):
    if x == 1 and n > 1:
        ans += 1
    elif x > 1 and x != n and n > 2:
        ans += 2
    elif x == n and n != 1:
        ans += 1    
    return ans
h, w = map(int, input().split())
r, c = map(int, input().split())
ans = 0
ans = adjacent(r, h, ans)
ans = adjacent(c, w, ans)
print(ans)