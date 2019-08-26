a = [1,3,4,5, 0]
b = a
c = a.copy()
print(a)
print(b)
print(c)
a.append(2)
a.pop(0)
a.pop(1)
print(a)
print(b)
print(c)
subc = c[1:4]
print(subc)
c.sort() # 升序排序
print(c)
c.reverse() # 倒序
print(c)
d = tuple(c)
print(d)

print(2*c)
print(2*d)
print(3*(2))
print(3*(2,))
# 当元组只有一个元素时末尾“，”不能省略

v = [1,3,4,6,2]
print(v)
