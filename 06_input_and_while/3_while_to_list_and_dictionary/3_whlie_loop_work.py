#熟食店
print("熟食店")
sandwich_orders = ['chacarero', 'pastrami', 'taco',
				'pastrami', 'tuna', 'pastrami']
finished_sandwiches = []

while sandwich_orders:
	finished_sandwich = sandwich_orders.pop()
	print("The " + finished_sandwich + " has been finished!")
	finished_sandwiches.append(finished_sandwich)
	
print("\nAll sandwiches have been finished!")


#五项烟熏牛肉卖完了
sandwich_orders = ['chacarero', 'pastrami', 'taco',
				'pastrami', 'tuna', 'pastrami']
finished_sandwiches = []
print("\n\n五项烟熏牛肉卖完了")

while 'pastrami' in sandwich_orders:
	sandwich_orders.remove('pastrami')
	
while sandwich_orders:
	finished_sandwich = sandwich_orders.pop()
	print("The " + finished_sandwich + " has been finished!")
	finished_sandwiches.append(finished_sandwich)
	
print("\nAll sandwiches have been finished!")


#梦想的度假胜地
print("\n\n梦想的度假胜地")
dream_resort = {}
flag = True
while flag:
	name = input("\nWhat is your name? ")
	question = input("If you could visit one place in the world, where would you go? ")

	dream_resort[name] = question
	repeat = input("Do you want another person to answer? (yes/no) ")
	
	if repeat == 'no':
		flag = False
		
print("\n-----Dream Resort-----")
for n, q in dream_resort.items():
	print(n.title() + "'s dream resort is " + q.title() + ".")
