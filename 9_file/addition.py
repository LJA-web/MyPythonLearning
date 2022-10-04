# 10-6 10-7
def add(x,y):
    try:
        res = int(x) + int(y)
    except:
        print("Please enter two numbers, not two characters.")
    else:
        print(res)

while True:
    x = input("Enter a number: ")
    y = input("Enter a number: ")
    if x=='exit' or y=='exit':
        break
    else:
        add(x,y)