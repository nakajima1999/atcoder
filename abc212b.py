x = input()
ans = 'Strong'
if x[0] == x[1] == x[2] == x[3]:
    ans = 'Weak'
else:
    weak = ['0123', '1234', '2345', '3456', '4567', '5678', '6789', '7890', '8901', '9012']
    if x in weak:
        ans = 'Weak'
print(ans)