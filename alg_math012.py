# アルゴリズムと数学 演習問題集
# 012 - Primality Test
def is_prime(i):
    if i <= 1:
        return False
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            return False
    return True

n = int(input())
if is_prime(n):
    print('Yes')
else:
    print('No')