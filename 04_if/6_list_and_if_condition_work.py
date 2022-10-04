#以特殊方式跟管理员打招呼
print("以特殊方式跟管理员打招呼")
users = ['admin', 'bile', 'cindy', 'duke', 'eric']
for user in users:
	if user == 'admin':
		print("Hello " + user.title() + ", would you like to see a status report?")
	else:
		print("Hello " + user.title() + ", thank you for logging in again.")


#处理没有用户的情形
print("\n\n处理没有用户的情形")
users = []
if users:
	for user in users:
		if user == 'admin':
			print("Hello " + user.title() + ", would you like to see a status report?")
		else:
			print("Hello " + user.title() + ", thank you for logging in again.")
else:
	print("We need to find some users!")
	

#检查用户名
print("\n\n检查用户名")
current_users = ['andy', 'bile', 'cindy', 'eric', 'franky']
new_users = ['Eric', 'franky', 'green', 'Helen', 'jordan']		#一个列表全部小写，另一个在比较时，将其变为小写比较
for new_user in new_users:
	if new_user.lower() in current_users:
		print("Please enter another username.")
	else:
		print("This username has not been used.")


#序数
print("\n\n序数")
numbers = list(range(1, 10))
for num in numbers:
	if num == 1:
		print(str(num) + "st")
	elif num == 2:
		print(str(num) + "nd")
	elif num == 3:
		print(str(num) + "rd")
	else:
		print(str(num) + "th")
