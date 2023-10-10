from online_manager.online_manager import OnlineManager
from  products.electronic import Electronic

class ElectronicOnlineManager(OnlineManager):
    def factory_method(self):
        return Electronic()
    