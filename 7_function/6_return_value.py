#城市名
print("城市名")
def city_country(city, country):
	city_country = city + ", " + country
	return city_country.title()
	
first = city_country("beijing", "china")
print(first)
second = city_country("xi'an", "china")
print(second)
third = city_country("new york", "america")
print(third)


#专辑
print("\n专辑")
def make_album(singer, album, num=''):
	album = {'singer':singer.title(), 'album':album.title()}
	if num:
		album['num'] = num
	return album
	
album_1 = make_album('jay chou', 'fantasy', '12')
print(album_1)
album_2 = make_album('maroon 5', 'Songs About Jane')
print(album_2)
album_3 = make_album('One Republic', 'dreaming out loud', '1')
print(album_3)


#用户的专辑
print("\n用户的专辑")
while True:
	print("\nPlease input your album(s):")
	print("(enter 'q' at any time to quit)")
	
	s = input("Singer:")
	if s == 'q':
		break
	a = input("Album:")
	if a == 'q':
		break
	n = input("Num:")
	if a == 'q':
		break
		
	album = make_album(s, a, n)
	print(album)
