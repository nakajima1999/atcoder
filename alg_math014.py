# アルゴリズムと数学 演習問題集
# 014 - Factorization
def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp % i==0:
            while temp % i== 0:
                temp //= i
                arr.append(str(i))

    if temp != 1:
        arr.append(str(temp))
    if arr == []:
        arr.append(str(n))
    return arr

n = int(input())
ans = ' '.join(factorization(n))
print(ans)