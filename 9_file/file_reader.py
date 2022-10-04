file_path = '9_file\pi.txt'
with open(file_path) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
    print("You birthday appears in the first million digits of pi!")
else:
    print("You birthday does not appear in the first million digits of pi.")