#外星人的颜色#1
print("外星人的颜色#1")
alien_color = 'green'
if alien_color == 'green':
	print("You get 5 points!")

print("\n另一种版本")
alien_color = 'red'
if alien_color == 'green':
	print("You get 5 points!")
	

#外星人的颜色#2
print("\n\n\n外星人的颜色#2")
alien_color = 'green'
if alien_color == 'green':
	print("You get 5 points!")
else:
	print("You get 10 points!")

print("\n另一种版本")
alien_color = 'red'
if alien_color == 'green':
	print("You get 5 points!")
else:
	print("You get 10 points!")


#外星人的颜色#3
print("\n\n\n外星人的颜色#3")
alien_color = 'green'
if alien_color == 'green':
	print("You get 5 points!")
elif alien_color == 'yellow':
	print("You get 10 points!")
else:
	print("You get 15 points!")

print("\n第二种")
alien_color = 'yellow'
if alien_color == 'green':
	print("You get 5 points!")
elif alien_color == 'yellow':
	print("You get 10 points!")
else:
	print("You get 15 points!")

print("\n第三种")
alien_color = 'red'
if alien_color == 'green':
	print("You get 5 points!")
elif alien_color == 'yellow':
	print("You get 10 points!")
else:
	print("You get 15 points!")


#人生的不同阶段
print("\n\n人生的不同阶段")
age = '48'
if age < '2':								#大于小于号后数字不要忘记加引号
	print("He is a baby.")
elif age < '4':
	print("He is a toddler.")
elif age < '13':
	print("He is a kid.")
elif age < '20':
	print("He is a teenager.")
elif age < '65':
	print("He is an adult.")
else:
	print("He is an older.")


#喜欢的水果
print("\n\n喜欢的水果")
favorite_fruits = ['apple', 'banana', 'peach', 'orange', 'grape']

if 'apple' in favorite_fruits:					#所查找找元素不要忘记加引号
	print("You really like apples!")
if 'banana' in favorite_fruits:
	print("You really like bananas!")
if 'peach' in favorite_fruits:
	print("You really like peachs!")
if 'orange'in favorite_fruits:
	print("You really like oranges!")
if 'grape' in favorite_fruits:
	print("You really like grapes!")
