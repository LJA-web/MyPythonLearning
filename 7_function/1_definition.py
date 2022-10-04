#greeter
def greet_user():
	"""显示简单的问候语"""
	print("Hello!")
	
greet_user()


print("\n")	
#向函数传递信息
def greet_user(username):
	"""显示简单的问候语"""
	print("Hello, " + username.title() + "!")
	
greet_user('jesse')
greet_user('Li jingan')


print("\n")
#实参和形参
#以上一个程序中，username就是一个形参，而jeese就是一个实参
