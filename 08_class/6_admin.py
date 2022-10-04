# 9-7
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


class Admin(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        print("Hello " + self.first_name + self.last_name +
              ", as an administer, you can:")
        for privilege in self.privileges:
            print("\t" + privilege)


admin1 = Admin("Tony", "Stark")
admin1.show_privileges()
