#s=set()
#print(s)
#print(s,type(s))

my_tuple = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
print("第三个元素：", my_tuple[2])
print("前三个元素：", my_tuple[:3])
print("最后三个元素：", my_tuple[-3:])
print("跳过一个元素：", my_tuple[::2])

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
combined_tuple = tuple1 + tuple2
print("组合后的元组：", combined_tuple)

first, *middle, last = combined_tuple
print("第一个元素：", first)
print("中间元素：", middle)
print("最后一个元素：", last)