#一个简单的字典
print("一个简单的字典")
alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])


#访问字典中的值
print("\n\n访问字典中的值")
alien_0 = {'color': 'green', 'points': 5}

new_points = alien_0['points']
print("You just earned " + str(new_points) + " points!")


#添加键-值对
print("\n\n添加键-值对")
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)


#修改字典中的值
print("\n\n修改字典中的值")
alien_0 = {'color': 'green'}
print("The alien is " + alien_0['color'] + ".")

alien_0['color'] = 'yellow'
print("The alien is now " + alien_0['color'] + ".")

#另一个更有趣的例子
print("\n另一个更有趣的例子")
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'fast'}
print("Original x_position: " + str(alien_0['x_position']))

#向右移动外星人
#据外星人移动速度决定将其移动的多远
if alien_0['speed'] == 'slow':
	x_increment = 1
elif alien_0['speed'] == 'medium':
	x_increment = 2
else:
	#这个外星人的速度一定很快
	x_increment = 3

#新位置等于老位置加上增量
alien_0['x_position'] = alien_0['x_position'] + x_increment

print("New x-position: " + str(alien_0['x_position']))


#删除键-值对(不可恢复)
print("\n\n添加键-值对")
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

del alien_0['points']
print(alien_0)


#由类似对象组成的字典
print("\n\n由类似对象组成的字典")
favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phli': 'python',
	}

print("Sarah's  favorite language is " +
	favorite_languages['sarah'].title() +
	".")
