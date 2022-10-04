#greet_users
def greet_users(names):
	"""向列表中每一位成员发出简单的问候"""
	for name in names:
		msg = "Hello, " + name.title() + "!"
		print(msg)
		
usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)


# 在函数中修改列表
print("\n在函数修改列表")
# 首先创建一个列表， 其中包含一些要打印的设计
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

# 模拟打印每个设计， 直到没有未打印的设计为止
#  打印每个设计后， 都将其移动到列表completed_models中
while unprinted_designs:
	current_designs = unprinted_designs.pop()
	
	#模拟根据设计制作3D打印模型的过程
	print("Printing model: " + current_designs)
	completed_models.append(current_designs)
	
# 显示打印好的所有模型
print("\nThe following models have been printed:")
for completed_model in completed_models:
	print("\t" + completed_model)

##########   高效率   ##########
print("\n高效率版本，代码存在差异，整体由两个函数组成")
def print_models(unprinted_designs, completed_models):
	"""
	模拟打印每个设计， 直到没有未打印的设计为止
	打印每个设计后， 都将其移动到列表completed_models中
	"""
	while unprinted_designs:
		current_designs = unprinted_designs.pop()
		
		#模拟根据设计制作3D打印模型的过程
		print("Printing model: " + current_designs)
		completed_models.append(current_designs)

def show_completed_models(completed_models):
	"""显示打印好的所有模型"""
	print("\nThe following models have been printed:")
	for completed_model in completed_models:
		print("\t" + completed_model)
		
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
show_completed_models(unprinted_designs)


#禁止函数修改列表##########################   较难理解的点
print("\n禁止函数修改列表")
def print_models(unprinted_designs, completed_models):
	"""
	模拟打印每个设计， 直到没有未打印的设计为止
	打印每个设计后， 都将其移动到列表completed_models中
	"""
	while unprinted_designs:
		current_designs = unprinted_designs.pop()
		
		#模拟根据设计制作3D打印模型的过程
		print("Printing model: " + current_designs)
		completed_models.append(current_designs)

def show_completed_models(completed_models):
	"""显示打印好的所有模型"""
	print("\nThe following models have been printed:")
	for completed_model in completed_models:
		print("\t" + completed_model)
		
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
print_models(unprinted_designs[:], completed_models)##############此处有变动
show_completed_models(completed_models)
show_completed_models(unprinted_designs)###########与上一个程序对比
