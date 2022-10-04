# 10-3 10-4
while True:
    guest = input("Enter your name: ")
    with open('9_file\guest.txt', 'a') as file_object:
        if guest!='exit':
            welcome = 'Helle ' + guest + "!"
            print(welcome)
            file_object.write(welcome + "\n")
        else:
            break
file_object.close()
print("Bye")