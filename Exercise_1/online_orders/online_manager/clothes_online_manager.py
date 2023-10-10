from online_manager.online_manager import OnlineManager
from  products.clothes import Clothes

class ClothesOnlineManager(OnlineManager):
    def factory_method(self):
        return Clothes()
    