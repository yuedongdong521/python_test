dic = {"name" : "python", "type" : "tools"}
print(dic)
dic["name"] = "Object-C"
print(dic)
dic["type"] = ""
print(dic)
dic["property"] = "动态语言"
print(dic)

# pop 删除指定key的键值对，
#popitem 随机删除键值对，当需要逐个删除字典中的键值对时使用popitem效率比较高
dic.pop("type")
print(dic)

dic1 = {"name":"ydd", "friends":['wyy', 'wry']}
# copy 浅复制
dic2 = dic1.copy()
# deepcopy 深复制
from copy import deepcopy
dic3 = deepcopy(dic1)

dic1["name"] = "ares"
dic1['friends'].remove("wry")
print("dic1 = ", dic1)
print("dic2 = ", dic2)
print("dic3 = ", dic3)

# fromkeys 创建一个新字典， 其中包含指定的key，默认值都为None
keys = {}.fromkeys(["name", "age"])
print(keys)

# get 使用get访问字典可以避免key不存在时的崩溃问题
print(dic.get("name"))
print(dic.get("type"))

# setdefault 添加键值对
dic.setdefault("works", 'N/A')

# items 获取字典中键值对组成的元组序列
dic_items = dic.items()
print(dic_items)
# 将字典的items转成list
dic_list = list(dic_items)
print("dic items list = ", dic_list)

# keys 获取所有key
keys = dic.keys()
print("keys = ", list(keys))

# values 获取所有values
values = dic.values()
print("values = ", list(values))

# update 添加新字典键值对
a = {"title" : "language"}
dic.update(a)
print(dic)

