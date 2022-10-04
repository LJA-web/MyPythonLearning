#人
man = {
	'first_name': 'li',
	'last_name': "jing'an",
	'age': 19,
	'city': 'anhui,wuwei',
	}
	
print(man['first_name'].title())
print(man['last_name'].title())
print(man['age'])
print(man['city'].title())


#喜欢的数字
print("\n\n喜欢的数字")
name_list = {
	'andy': '3',
	'bile': '4',
	'cindy': '6',
	'eric': '7',
	'frank': '8',
	}
	
print("Andy's favorite number is " +
	name_list['andy'] +
	".")
print("Bile's favorite number is " +
	name_list['bile'] +
	".")
print("Cindy's favorite number is " +
	name_list['cindy'] +
	".")
print("Eric's favorite number is " +
	name_list['eric'] +
	".")
print("Frank's favorite number is " +
	name_list['frank'] +
	".")


#词汇表
print("\n\n词汇表")
words = {
	'title': '单词首字母大写',
	'upper': '单词所有字母大写',
	'lower': '单词所有字母小写',
	'rstrip': '去除单词后空白',
	'lstrip': '去除单词前空白',
	}

print("title: " + words['title'])
print("upper: " + words['upper'])
print("lower: " + words['lower'])
print("rstrip: " + words['rstrip'])
print("lstrip: " + words['lstrip'])
