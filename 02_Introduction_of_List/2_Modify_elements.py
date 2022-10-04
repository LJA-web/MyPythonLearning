#修改
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)
print("\n")


#添加   .append('name')
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles.append('ducati')
print(motorcycles)
print("\n")


#插入   .insert(location, 'name')
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles.insert(0, 'ducati')
print(motorcycles)
print("\n")


#删除   del name[location]法（单个删除指定位置元素）
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
del motorcycles[1]
print(motorcycles)
print("\n")
#删除   .pop(location)法（未指明位置时，单个删除末尾元素）
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
popped_motorcycles = motorcycles.pop()
last_motorcycles = popped_motorcycles
print(motorcycles)
print(popped_motorcycles)
print("The last moyorcycle I owned was a " + last_motorcycles.title() + ".")
print("\n")
#删除   .remove('name')法（单个删除指定名称元素）
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
too_expensive = "yamaha"
motorcycles.remove(too_expensive)
print(motorcycles)
print("A " + too_expensive.title() + " is too enpensive for me.")
print("\n")
