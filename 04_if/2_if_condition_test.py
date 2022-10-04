#条件测试
name = 'Bile'
if name == 'Bile':
	print("Is his name Bile? I predict Ture.")
else:
	print("No, his name is Bile")


#检查两个字符串相等和不等
print("\n\n检查两个字符串相等")
name_1 = 'Andy'
name_2 = 'andy'
if name_1 == name_2.title():
	print("The two names are the same. means ture")
else:
	print("They are two different names. means flase")
	
print("\n检查两个字符串不相等")
food_1 = 'duck'
food_2 = 'duck'
if food_1 != food_2:
	print("They are two different foods. means ture")
else:
	print("The two foods are the same. means flase")
	

#检查两个数字的大小关系
print("\n\n检查两个数字的大小关系")
num_1 = 100
num_2 = 101
if num_1 == num_2:
	print("Ture")
else:
	print("Flase")


#使用关键字and和or的测试
print("\n\n使用关键词and测试")
age_3 = 18
age_4 = 20
if (age_3 <=18) and (age_4 <=18):
	print("T")
else:
	print("F")
	
print("\n使用关键词or测试")
age_3 = 18
age_4 = 20
if (age_3 <=18) or (age_4 <=18):
	print("T")
else:
	print("F")



#测试特定的值是否包含或不包含在列表中
print("\n\n测试特定的值是否包含在列表中")
menu = ['steak', 'pork', 'carrot']
if 'duck' in menu:
	print("Ture")
else:
	print("Flase")
	
print("\n测试特定的值是否不包含在列表中")
menu = ['steak', 'pork', 'carrot']
if 'duck' not in menu:
	print("Ture")
else:
	print("Flase")
