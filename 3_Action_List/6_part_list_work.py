#切片
print("切片：")
students = ['alice', 'bile', 'cindy', 'duke', 'eric', 'frank', 'green', 'helen', 'jordan']

print("The first three students in the list are:")
print(students[:3])

print("\nThree students from the middle of the list are:")
print(students[3:6])

print("The last three students in the list are:")
print(students[-3:])


#你的披萨和我的披萨
print("\n\n我的披萨和朋友的披萨：")
my_pizzas = ['Pizza Hut', 'Papa Johns', "Domino's Pizza"]
friend_pizzas = my_pizzas[:]

my_pizzas.append('KFC')
print("My favorite pizzas are:")
for pizza in my_pizzas:
	print(pizza)

friend_pizzas.append("McDonald's")
print("\nMy friend favorite pizzas are:")
for pizza in friend_pizzas:
	print(pizza)


#使用多个循环
print("\n\n使用多个循环：")
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append("cannoli")			#再根据个人喜好添加元素
friend_foods.append('ice cream')

print("My favorite foods are:")
for food in my_foods:
	print(food)

print("\nMy friend's favorite foods are:")
for food in friend_foods:
	print(food)
