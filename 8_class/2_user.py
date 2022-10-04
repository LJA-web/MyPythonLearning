# 9-3
class User:
    def __init__(self, first_name, last_name):
        """初始化"""
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        print("My first name is " + self.first_name.title() + ".")
        print("My last name is " + self.last_name.title() + ".")

    def greet_user(self):
        print("Have a good day, " + self.first_name.title()
              + self.last_name.title() + "!")


user_1 = User('stephen', 'green')
user_1.describe_user()
user_1.greet_user()
