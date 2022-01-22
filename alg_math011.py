# アルゴリズムと数学 演習問題集
# 011 - Print Prime Numbers
def is_prime(i):
    if i <= 1:
        return False
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            return False
    return True

def prime_list(n):
    lst = []
    for i in range(n):
        if is_prime(i + 1):
            lst.append(i + 1)
    return lst
n = int(input())
prime_list = prime_list(n)
prime_list = [str(e) for e in prime_list]
ans = ' '.join(prime_list)
print(ans)