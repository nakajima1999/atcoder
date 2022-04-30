# AtCoder Beginner Contest 244
# B - Go Straight and Turn Right
n = int(input())
t = input()
xy = [0, 0]
a = 0  # 向いてる方向
direction = {
    0: [0, 1],  # 0: 東（x += 1）
    1: [1, -1], # 1: 南（y -= 1）
    2: [0, -1], # 2: 西（x -= 1）
    3: [1, 1],  # 3: 北（y += 1）
    }

for s in t:
    if s == 'S':
        xy[direction[a][0]] += direction[a][1]
    else:
        a += 1
        a %= 4
print(xy[0], xy[1])