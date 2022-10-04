#T恤
def T(size, sentence):
	print(size + "   " + sentence)
	
T('L', 'the best one')


#
print("\n")
def T(size, sentence='I love python'):
	print(size + "   " + sentence)
	
T('M')
T('L', sentence='U')


#城市
print("\n")
def describe_city(name, country='iceland'):
	print(name.title() + " is in " + country.title() + ".")
	
describe_city('reykjavik')
describe_city('beijing', country='china')
describe_city("xi'an", country='china')
