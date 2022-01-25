# アルゴリズムと数学 演習問題集
# 014 - Factorization
def factorization(n):
    arr = []
    temp = n  # nを素数で割っていく
    for i in range(2, int(-(-n ** 0.5 // 1)) + 1):
        if temp % i == 0:  # iで割り切れる場合
            while temp % i == 0:  # tempをiで割れるだけ割る
                temp //= i
                arr.append(str(i))
    
    if temp != 1:  # 最終的なtempが1以外の場合，素数であるため追加
       arr.append(str(temp))
    if arr == []:  # arrがからの場合，n自体が素数であるため追加
        arr.append(str(n))
    return arr

n = int(input())
ans = ' '.join(factorization(n))
print(ans)