website = 'http://www.python.org'
# 字符串是不可变类型，元素赋值和切片赋值都是非法操作
# website[-3:] = 'com'

# 字符串格式
format = 'hello, %s. %s enough for ya?'
values = ('world', 'hot')
print("format = %s" % (format % values,))

# 替换字段没有将索引用作名称
indexStr = "{}, {} and {}".format("first", "second", "third")
print("indexStr = %s" % indexStr)

# 字符串按照索引排序
index2Str = "{1} {2} {0} {3} {1}".format('zore','first', 'second', 'third')
print('index2Str = %s' % index2Str)

# 命名字段
from math import pi
piTest = "{name} is approximatelyc {value:.2f}.".format(value=pi, name = "圆周率")
print(piTest)

pitest1 = "{name} is approximatelyc {value}.".format(value=pi, name='圆周率')
print(pitest1)

# 命名字段 简写，在前面加f
pitest2 = f"圆周率 is approximatelyc {pi}."
print(pitest2)

# 宽度 (数字和字符串对齐方式不一样)
widthNum = "{num:10}".format(num = 3)
print("widthNum = ", widthNum)
widthStr = "{str:10}".format(str = 'abc')
print("widthStr = ", widthStr)

# 千位分隔符 同时指定其他格式设置元素时，这个逗号应放在宽度和表示精度的句点之间
googol = "one googol is {:,}".format(10**10)
print("千位分隔符 ： ", googol)
# 同时指定其他格式设置元素时，这个逗号应放在宽度和表示精度的句点之间
from math import e
eStr = "100e = {:,.2f}".format(e*10000)
print(eStr)

# 对齐方式
pi1 = '{:010.2f}'.format(pi) # 十位数，保留两位小数，用0补齐
print("pi1 = ", pi1)
pi2 = '{:8.2f}'.format(pi)
print("pi2 = ", pi2)
# 要指定左对齐、右对齐和居中，可分别使用<、>和^
print("{0:<10.2f}\n{0:^10.2f}\n{0:>10.2f}".format(pi))

# 指定填充字符
print("{:$<10}\n{:$^10}\n{:$>10}".format("ydd", "wyy", "dy"))

# 字符串方法
# 1.center 通过在两边添加填充字(默认为空格)让字符串居中
centerStr = "the middle by Ares Eat World"
print(centerStr.center(39))
print(centerStr.center(39, "*"))

# 2. find 在字符串中查找子串。如果找到，就返回子串的第一个字符串的索引，否则返回-1
print(centerStr.find("wyy"))
print(centerStr.find("ares"))
print(centerStr.find("Ares"))

# 3. join 合并序列元素
seq = [1,2,3,4]
sep = "+"
# print(sep.join(seq)) #只能合并字符序列，所有的元素只能是字符串
seq = ["1", "2", "3", "4"]
print(sep.join(seq))

# 4. lower 将字符串中的大写字母转成小写
print(centerStr.lower())
print("i love eat".title()) # title函数将字符串首字母大写

# 5. replace 替换字符串
rep = "this is a test."
print(rep.replace('is', 'an'))
print(rep.replace('i', "I"))

# 6. split 拆分字符串，与join相反
print(centerStr.split(" "))

# 7. strip 将字符串头部和尾部的空白删除，不会删除中间的空白，返回删除后的结果
print("  this a strip mothon.  ".strip())

# 8. translate
# 方法translate与replace一样替换字符串的特定部分，但不同的是它只能进行单字符替换。
# 这个方法的优势在于能够同时替换多个字符，因此效率比replace高。
# 使用translate前必须创建一个转换表。这个转换表指出了不同Unicode码点之间的转 换关系。
# 要创建转换表，可对字符串类型str调用方法maketrans，
# 两个参数:两个 长度相同的字符串，它们指定要将第一个字符串中的每个字符都替换为第二个字符串中的相应字符
table = str.maketrans('cs', 'kz') # 创建转换表
print(table) # Unicode码的映射
print("this is an incredible test".translate(table))
print("this is an incredible test".translate(table))
table2 = str.maketrans('i', "I")
print(table2)
print("this is an incredible test".translate(table2))






