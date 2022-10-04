#函数 range(其实数值, 结尾数值)   结尾数值并不会被打印
for value in range(1, 5):
	print(value)

print("\n\n")
#函数list() 直接将range()的结果直接转化为列表
numbers = list(range(1, 5))
print(numbers)

#打印双数
even_numbers = list(range(2, 11, 2))
print(even_numbers)

#打印前10个整数的平方，不能通过步长来控制，就通过计算.append()方法添加到自己定义的列表之中
squares = []
for value in range(1, 11):
	square = value**2
	squares.append(square)
	
print(squares)
#以上结果输出的另一种方法
squares = [value**2 for value in range(1, 11)]
print("\n通过另一种方法打印前10个整数的平方：")
print(squares)

print("\n\n")
#最小值min()函数、最大值max()函数、求和sum()函数
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(num)
print("min = " + str(min(num)))
print("max = " + str(max(num)))
print("sum = " + str(sum(num)))
