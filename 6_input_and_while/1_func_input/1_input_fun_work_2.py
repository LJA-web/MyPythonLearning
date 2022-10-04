#餐馆订位
restaurant = input("How many people are dining? ")
restaurant = int(restaurant)

if restaurant > 8:
	print("\nNo empty table at this time.")
else:
	print("\nThere are some empty tables.")
