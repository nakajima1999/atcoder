n = int(input())
for k in range(1, 10 ** 18):    
    if 2 ** k > n:
        break
print(k - 1)