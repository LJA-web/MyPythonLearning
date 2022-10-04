#一个简单示例
cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
	if car == 'bmw':
		print(car.upper())
	else:
		print(car.title())


#条件测试
#检查是否相等
print("\n\n检查是否相等：")
car = 'bmw'
if car == 'bmw':
	print("\nTrue")
else:
	print("\nFlase")
print(car)

car = 'audi'
if car == 'bmw':
	print("\nTrue")
else:
	print("\nFlase")
print(car)

car = 'BMW'
if car == 'bmw':
	print("\nTrue")
else:
	print("\nFlase")
print(car)

car = 'BMW'
if car.lower() == 'bmw':
	print("\nTrue")
else:
	print("\nFlase")
print(car)


#检查是否不相等
print("\n\n检查是否不相等")
requested_topping = 'mushroom'

if requested_topping != 'anchovies':		#意式小银鱼
	print("Hold the anchovies!")


#比较数字
print("\n\n比较数字")
answer = 17
if answer < 21:
	print("True")
else:
	print("Flase")

if answer <= 21:
	print("True")
else:
	print("Flase")

if answer == 21:
	print("True")
else:
	print("Flase")

if answer > 21:
	print("True")
else:
	print("Flase")

if answer >= 21:
	print("True")
else:
	print("Flase")
	

#检查多个文件
print("\n\n检查多个文件\nand语句")
age_0 = 22
age_1 = 18
if age_0 >= 21 and age_1 >= 21:
	print("True")
else:
	print("Flase")
	
age_0 = 22
age_1 = 22
if (age_0 >= 21) and (age_1 >= 21):
	print("True")
else:
	print("Flase")
	
print("\nor语句")
age_0 = 22
age_1 = 18
if age_0 >= 21 or age_1 >= 21:
	print("True")
else:
	print("Flase")
	
age_0 = 18
age_1 = 18
if (age_0 >= 21) or (age_1 >= 21):
	print("True")
else:
	print("Flase")


#检查特定值是否包含在列表中
print("\n\n检查特定值是否包含在列表中")
requested_toppings = ['mushrooms', 'onions', 'pineapple']
if 'mushrooms' in requested_toppings:
	print("True")
else:
	print("Flase")

if 'pepperoni' in requested_toppings:
	print("True")
else:
	print("Flase")


#检查特定值是否不包含在列表中
print("\n\n检查特定值是否包含在列表中")
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
	print(user.title() + ",you can post a reponse if you wish.")
