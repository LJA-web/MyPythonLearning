subject = ['chainese', 'math', 'english', 'physics', 'chemistry', 'biology']
print("顺序输出元素：")
print(subject[0])
print(subject[1])
print(subject[2])
print(subject[3])
print(subject[4])
print(subject[5] + '\n')

#通过将索引指定为-1、-2、-3，让python分别返回倒数第一、倒数第二、倒数第三个元素
#以此类推
print("逆序输出元素：")
print(subject[-1])
print(subject[-2])
print(subject[-3])
print(subject[-4])
print(subject[-5])
print(subject[-6] + '\n')

#使用列表中各值
message = "My favorite subject is " + subject[1].title() + "."
print(message)
