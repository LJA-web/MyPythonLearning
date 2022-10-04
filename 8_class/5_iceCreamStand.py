# 9-6
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


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors=["ice", "cream"]

    def show_flavors(self):
        print(self.flavors)

stand1 = IceCreamStand("First stand", "cold drink")
stand1.show_flavors()