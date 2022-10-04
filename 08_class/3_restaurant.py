# 9-4
class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        """初始化，传入饭店名称和菜的类型"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        # 直接设置默认值
        self.number_served = 0

    def set_number_served(self, numbers):
        """设置就餐人数"""
        self.number_served = numbers

    def increment_number_served(self, increasement):
        """设置增加的就餐人数"""
        self.number_served += increasement


restaurant = Restaurant('Great Dining Hall', 'huicai')
print("12:00  -- There are " +
      str(restaurant.number_served) + " people having lunch.")
restaurant.set_number_served(5)
print("12:10  -- There are " +
      str(restaurant.number_served) + " people having lunch.")
restaurant.increment_number_served(30)
print("12:30  -- There are " +
      str(restaurant.number_served) + " people having lunch.")
