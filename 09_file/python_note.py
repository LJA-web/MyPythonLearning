# 10-1 10-2
file_path = '9_file\learning_python.txt'
with open(file_path) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.strip())

for line in lines:
    print(line.replace('Python','C++').strip())