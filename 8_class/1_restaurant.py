# 9-1,9-2
class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        """初始化，传入饭店名称和菜的类型"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """打印简单的信息"""
        print("Hello sir/lady")
        print("Welcome to " + self.restaurant_name.title() + ".")
        print("We have " + self.cuisine_type + ".")

    def open_restaurant(self):
        """告诉大家我们正在营业"""
        print("OPENING!")


my_restaurant = Restaurant('Great Dining Hall', 'huicai')
# 调用方法的时候，不要忘记给方法后面加上括号！！！
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()
