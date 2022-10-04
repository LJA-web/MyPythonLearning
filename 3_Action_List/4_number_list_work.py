#数到20
print("数到20：")
for value in range(1, 21):
	print("\t" + str(value))


#一百万
#print("\n\n一百万：")
#millions = list(range(1, 1000001))
#for num in millions:
#	print(num)


#计算1~1000000的总和
print("\n\n计算1~1000000的总和：")
millions = [value for value in range(1, 1000001)]
print("\t\t   min = " + str(min(millions)))
print("\t\t   max = " + str(max(millions)))
print("\t\t   sum = " + str(sum(millions)))


#奇数
print("\n\n1~20以内的奇数：")
odd_number = list(range(1, 20, 2))
for num in odd_number:
	print("\t" + str(num))


#3的倍数
print("\n\n3的倍数：")
numbers = list(range(3, 31, 3))
for num in numbers:
	print("\t" + str(num))


#立方
print("\n\n立方：")
cube = []
for value in range(3, 31, 3):
	cube.append(value)
print("\t" + str(cube))


#立方解析
print("\n\n立方解析：")
cube = [value**3 for value in range(1, 11)]
print("\t" + str(cube))
