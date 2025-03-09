s='helloworld'
print(s[-1:-11:-1])


numbers = [1, 2, 3, 4, 5]
print("数字列表：", numbers)


fruits = ["apple", "banana", "cherry"]
print("水果列表：", fruits)


my_list = [10, 20, 30, 40, 50]

my_list.append(60)
print("添加元素后：", my_list)

my_list.insert(2, 25)
print("插入元素后：", my_list)

my_list.remove(30)
print("删除元素后：", my_list)

my_list[0] = 100
print("修改元素后：", my_list)

print("列表长度：", len(my_list))

print("元素40的索引：", my_list.index(40))