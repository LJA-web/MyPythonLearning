#10的整数倍
number = input("Enter a number, and I'll tell you if it's 10 integer times: ")
number = int(number)

if number %10 == 0:
	print("\nThis number is 10 integer times.")
else:
	print("\nThis number is not 10 integer times.")
