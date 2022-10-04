#人
print("人")
boy_1 = {
	'first_name': 'li',
	'last_name': "jing'an",
	'age': 19,
	'city': 'anhui,wuwei',
	}

boy_2 = {
	'first_name': 'shen',
	'last_name': 'yang',
	'age': 19,
	'city': 'anhui,wuwei',
	}
	
boy_3 = {
	'first_name': 'tong',
	'last_name': 'yang',
	'age': 19,
	'city': 'anhui,wuwei',
	}
	
boys = [boy_1, boy_2, boy_3]
for boy in boys:
	print(boy)


#宠物
print("\n\n宠物")
dog = {
	'type': 'gold',
	'master': 'andy',
	}
cat = {
	'type': 'blue cat',
	'master': 'bile',
	}
duck = {
	'type': 'cole',
	'master': 'cindy',
	}
	
pets = [dog, cat, duck]

for pet in pets:
	print(pet)


#喜欢的地方
print("\n\n喜欢的地方")
favorite_places = {
	'andy': ['beijing', 'hefei', 'huangshan'],
	'bile': ['shanghai', 'guangzhou', 'xizang'],
	'cindy': ["xi'an", 'xianyang', 'changsha'],
	}

for name, place in favorite_places.items():
	print(name.title() + "'s favorite places are:")
	for p in place:
		print("\t\t" + p.title())
	print("\n")


#喜欢的数字
print("\n\n喜欢的数字")
name_list = {
	'andy': ['3', '6'],
	'bile': ['4', '3'],
	'cindy': ['6', '8'],
	'eric': ['7', '0'],
	'frank': ['8', '9'],
	}
	
for name, nums in name_list.items():
	print(name.title() + "'s favorite numbers are:")
	for num in nums:
		print("\t\t\t    " + num)
	print("\n")


#城市
cities = {
	'beijing': {
		'country': 'china',
		'populationg': '4,299,000',
		'fact': 'capital'},
	'new york': {
		'country': 'america',
		'populationg': '8,300,000',
		'fact': "the world's largest city"},
	'tokyo': {
		'country': 'japan',
		'populationg': '8,336,599',
		'fact': "capital"},
	}

for k, v in cities.items():
    print(k + ": " + str(v))

print("\n")
for city, messages in cities.items():
	print("There are some messages about " + 
		name.title() + ":")
	for message_k, message_v in messages.items():
		print("\t\t" + message_k + ": " + message_v.title())
	print("\n")
