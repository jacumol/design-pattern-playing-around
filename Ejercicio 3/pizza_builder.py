from abc import ABC, abstractmethod

class PizzaBuilder(ABC):
    @abstractmethod
    def set_size(self, size):
        pass

    @abstractmethod
    def set_crust(self, crust):
        pass

    @abstractmethod
    def set_topping(self, topping):
        pass
    
    @abstractmethod
    def set_cheesy_crust(self, cheesy_crust):
        pass
