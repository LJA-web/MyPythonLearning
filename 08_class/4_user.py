# 9-5
class User:
    def __init__(self, first_name, last_name):
        """初始化"""
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0

    def increment_login_attempts(self):
        """使 login_attempts 加 1"""
        self.login_attempts += 1
        print("There (is)are " + str(self.login_attempts) + " login attempt(s).")

    def reset_login_attempts(self):
        """将 login_attempts 置 0"""
        self.login_attempts = 0
        print("There (is)are " + str(self.login_attempts) + " login attempt(s).")


user_1 = User('stephen', 'green')
print("There (is)are " + str(user_1.login_attempts) + " login attempt(s).")
user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.reset_login_attempts()
