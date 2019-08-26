
a = [0,1]
b = 0
for index in range(10):
    b += (a[-1] + a[-2])
    a.append(a[-2] + a[-1])
print(b)
print(a)
