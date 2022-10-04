#位置实参
print("位置实参")
def describe_pet(animal_type, pet_name):
	"""显示宠物信息"""
	print("\nI have a " + animal_type + ".")
	print("My " + animal_type + "'s name is " + pet_name.title() + ".")
	
describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')


#关键字实参(以下两行等价)
print("\n关键字实参")
describe_pet(animal_type="dog", pet_name='willie')
describe_pet(pet_name='willie', animal_type="dog")


#默认值
print("\n默认值")
def describe_pet(pet_name, animal_type='dog'):
	"""显示宠物信息"""
	print("I have a " + animal_type + ".")
	print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet('willie')


#等效的函数调用（以下两个调用函数代码等价）
print("\n等效的函数调用")
describe_pet('willie')
describe_pet(pet_name = 'willie')
