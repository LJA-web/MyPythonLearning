#返回简单值
print("返回简单值")
def get_formatted_name(first_name, last_name):
	"""返回整洁的姓名"""
	full_name = first_name + ' ' + last_name
	return full_name.title()
	
musician = get_formatted_name('jimi', 'hendrix')
print(musician)


#让实参变成可选的
print("\n让实参变成可选的")
def get_formatted_name(first_name, middle_name, last_name):
	"""返回整洁的姓名"""
	full_name = first_name + ' ' + middle_name + ' ' + last_name
	return full_name.title()
	
musician = get_formatted_name('john', 'lee', 'hooker')
print(musician)

def get_formatted_name(first_name, last_name, middle_name=''):
	"""返回整洁的姓名"""
	if middle_name:
		full_name = first_name + ' ' + middle_name + ' ' + last_name
	else:
		full_name = first_name + ' ' + last_name
	return full_name.title()
	
musician = get_formatted_name('jimi', 'hendrix')
print(musician)
musician = get_formatted_name('john', 'lee', 'hooker')
print(musician)


#返回字典
print("\n返回字典")
def bulid_person(first_name, last_name, age=''):
	"""返回一个字典，其中包含有关一个人的信息"""
	person = {'first':first_name, 'last':last_name}
	if age:
		person['age'] = age
	return person
	
musician = bulid_person('jimi', 'hendrix', '27')
print(musician)


#结合使用函数和while循环
print("\n结合使用函数和while循环")
def get_formatted_name(first_name, last_name):
	"""返回整洁的姓名"""
	full_name = first_name + ' ' + last_name
	return full_name.title()
#这是一个无限循环，若加上while循环需要缩进以下代码
while True:
	print("\nPlease tell me your name:")
	print("(enter 'q' at any time to quit)")
	
	f_name = input("First name:")
	if f_name == 'q':
		break
	l_name = input("Last name:")
	if l_name == 'q':
		break
		
	formatted_name = get_formatted_name(f_name, l_name)
	print("\nHello, " + formatted_name + "!")

