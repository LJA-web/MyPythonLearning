#词汇表2
print("词汇表2")
words = {
	'title': '单词首字母大写',
	'upper': '单词所有字母大写',
	'lower': '单词所有字母小写',
	'rstrip': '去除单词后空白',
	'lstrip': '去除单词前空白',
	}

for key, value in words.items():
	print(key + ": " + value)


#河流
print("\n\n河流")
rivers = {
	'nile': 'egypt',
	'yellow river': 'chain',
	'yangtze': 'chain',
	}
	
for k, v in rivers.items():
	print("The " + k.title() + " runs through " + v.title() + ".")

print("\n输出河流名字")
for key in rivers.keys():
	print(key.title())

print("\n输出国家名字")
for value in rivers.values():
	print(value.title())


#调查
print("\n\n调查")
favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
	}

respondents = ['andy', 'bile', 'cindy', 'edward', 'jen']

for name in respondents:
	if name in favorite_languages.keys():
		print(name.title() + ", thanks for you help!")
	else:
		print("Hello " + name.title() + 
			", can we investigate some questions? ")
