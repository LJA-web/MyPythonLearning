#遍历所有的键-值对
#即使遍历字典，键-值对的返回顺序也与存储顺序不同
#Python不关心键-值对的存储顺序，而只跟踪键和值之间的关联关系
print("遍历所有键-值对")
user_0 = {
	'username': 'efermi',
	'first': 'enrico',
	'last': 'fermi',
	}
	
for key, value in user_0.items():
	print("\nKey: " + key)
	print("Value: " + value)
	
#另一个例子
print("\n另一个例子")
favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
	}
	
for name, language in favorite_languages.items():
	print(name.title() + "'s favorite languages is " +
	language.title() + ".")


#遍历字典中的所有键  .keys()
print("\n\n遍历字典中的所有键")
favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
	}
	
for name in favorite_languages.keys():
	print(name.title())
		
#另一个例子
print("\n另一个例子")
favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
	}

friends = ['phil', 'sarah']
for name in favorite_languages:
	print(name.title())
	
	if name in friends:
		print("Hi " + name.title() +
			", I see your favorite languages is " +
			favorite_languages[name].title() + "!")

#又一个例子
print("\n又一个例子")
favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
	}

if 'erin' not in favorite_languages.keys():
	print("Erin, please take our poll!")


#按顺序遍历字典中的所有键
print("\n\n按顺序遍历字典中的所有键")
favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
	}

for name in sorted(favorite_languages.keys()):
	print(name.title() + ", thank you for taking the poll.")


#遍历字典中的所有值  .values()
print("\n\n遍历字典中的所有值")
favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
	}

print("The following languages have been metioned:")
for language in favorite_languages.values():
	print(language.title())

#要求输出名字唯一
print("\n\n要求输出名字唯一")
favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
	}

print("The following languages have been metioned:")
for language in set(favorite_languages.values()):
	print(language.title())
