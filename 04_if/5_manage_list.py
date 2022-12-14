#检查特殊元素
print("检查特殊元素")
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
	if requested_topping == "green peppers":
		print("Sorry, we are out of green peppers right now.")
	else:
		print("Adding " + requested_topping + ".")
	
print("\nFinished making your pizza!")


#确定列表不是空的
print("\n\n确定列表不是空的")
requested_toppings = []

if requested_topping:
	for requested_topping in requested_toppings:
		print("Adding " + requested_topping + ".")
	print("\nFinished making your pizza!")
else:
	print("\nAre you sure you want a plain pizza?")


#使用多个列表
print("\n\n使用多个列表")
available_toppings = ['mushrooms', 'olives', 'green peppers',
					   'pepperoni', 'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
	if requested_topping in available_toppings:
		print("Adding " + requested_topping + ".")
	else:
		print("Sorry, we don't have " + requested_topping + ".")

print("\nFinished making your pizza!")
