#让用户选择何时退出
prompt = "Tell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program.  "

message = ""
while message != 'quit':
	message = input(prompt)
	
	if message != 'quit':			#这两行代码目的是当输入quit时不显示 quit
		print(message)
