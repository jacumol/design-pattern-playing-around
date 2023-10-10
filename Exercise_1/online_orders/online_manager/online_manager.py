from __future__ import annotations
from abc import ABC, abstractmethod

class OnlineManager(ABC):
    @abstractmethod
    def factory_method(self):
        pass
    
    def sell_product(self):
        product = self.factory_method()
        print(product.inventory_check())
        print(product.invoice())
        print(product.notify_client())
