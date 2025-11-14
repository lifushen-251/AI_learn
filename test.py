# 创建空集合
Set=set()    #定义空集合
print(type(Set))

#添加一个元素
Set.add("114")
print(Set)

#将一个可迭代对象依次加到集合中
Set.update([1, '1', '4'])
print(Set)
