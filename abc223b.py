# AtCoder Beginner Contest 223
# 	B - String Shifting
s = input()
list_shift_s = []
for i in range(len(s)):
    shift_s = s[i:] + s[:i]
    list_shift_s.append(shift_s)

list_shift_s.sort()
print(list_shift_s[0])
print(list_shift_s[-1])