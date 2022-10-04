def prime(num):
	for i in list(range(2,num)):
		flag = 1
		if num%i != 0:
			flag = 1
		else:
			flag = 0
			break
	if flag == 1:
		print(str(num) + "是素数。")
		for i in list(range(2,num)):
			if num%i != 0:
				print(str(i))

	else:
		print(str(num) + "不是素数。")
	return flag

num = input("请输入一个整数：")
num = int(num)
prime(num)
