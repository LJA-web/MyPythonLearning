#按首字母顺序排列     .sort()永久性改变，无法变回原来的顺序
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print("Here is the order list:")
print(cars)

#按首字母顺序排列  赋予.sort()参数  reverse = True，即可按首字母逆序排列
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse = True)
print("\nHere is the reverse order list:")
print(cars)

print("\n\n")
#以上两个都是永久排序，下面介绍临时排序     函数sorted()
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the oringinal list again:")
print(cars)

print("\n\n")
#倒着输出列表,永久性改变，可再次使用 .reverse（） 将列表再次倒序输出
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)

cars.reverse()
print(cars)

print("\n")
#确定列表长度,也可理解为列表元素个数，且从 1 开始计数     函数len()
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(len(cars))
