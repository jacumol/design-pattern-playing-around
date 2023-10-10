from online_manager.online_manager import OnlineManager
from  products.food import Food

class FoodOnlineManager(OnlineManager):
    def factory_method(self):
        return Food()
    
    def sell_product(self):
        product = self.factory_method()
        print(product.inventory_check())
        print(product.invoice())
        print(product.notify_client())
        print(product.manage_frozen())