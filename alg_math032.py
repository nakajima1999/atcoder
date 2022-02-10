# アルゴリズムと数学 演習問題集
# 032 - Binary Search
n, x = map(int, input().split())
a = set(list(map(int, input().split())))
if x in a:
    print('Yes')
else:
    print('No')