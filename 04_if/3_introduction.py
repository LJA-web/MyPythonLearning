#简单的if语句
print("简单的if语句")
age = 19
if age >= 18:
	print("You are old enough to vote!")
	print("Have you registered to vote yet?")


#if-else语句
print("\n\nif-else语句")
age = 17
if age >= 18:
	print("You are old enough to vote!")
	print("Have you registered to vote yet?")
else:
	print("Sorry, you are too young to vote.")
	print("Please register to vote as soon as you turn 18!")


#if-elif-else语句
print("\n\nif-else-else语句")
age = 12
if age < 4:
	print("You admission cost is $0")
elif age < 18:
	print("You admission cost is $5")
else:
	print("You admission cost is $10")

#另一种简介写法
print("\n另一种简介写法")
age = 12

if age < 4:
	price = 0
elif age < 18:
	price = 5
else:
	price = 10
print("You admission cost is $" + str(price) + ".")


#使用多个elif代码块
print("\n\n使用多个elif代码块")
age = 66

if age < 4:
	price = 0
elif age < 18:
	price = 5
elif age < 65:
	price = 10
else:
	price = 5
print("You admission cost is $" + str(price) + ".")


#省略else代码块
print("\n\n省略else代码块")
age = 66

if age < 4:
	price = 0
elif age < 18:
	price = 5
elif age < 65:
	price = 10
elif age >= 65:
	price = 5
print("You admission cost is $" + str(price) + ".")


#测试多个条件
print("\n\n测试多个条件")
requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
	print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
	print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
	print("Adding extro cheese.")

print("\nFinished making your pizza!")
