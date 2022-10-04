#切片
print("切片：")
players = ['charles', 'martina', 'micheal', 'florence', 'eli']
print(players[0:3])

print(players[1:4])#可输出任意片段

print(players[:4])#没有起始值默认从头开始

print(players[2:])#没有末尾值默认到末尾结束

print(players[-3:])#打印后三位成员名单


#遍历切片
print("\n\n遍历切片：")
players = ['charles', 'martina', 'micheal', 'florence', 'eli']
print("Here are the first there players on my team:")
for player in players[:3]:
	print("\t\t\t\t\t\t" + str(player.title()))


#复制列表，复制并非直接赋值，否则复制体会随着本体变化而变化
print("\n\n复制列表：")
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append("cannoli")			#再根据个人喜好添加元素
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)
