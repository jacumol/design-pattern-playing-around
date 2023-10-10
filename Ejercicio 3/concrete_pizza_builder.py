from pizza import Pizza
from pizza_builder import PizzaBuilder

class ConcretePizzaBuilder(PizzaBuilder):
    def __init__(self):
        self.pizza = Pizza()

    def set_size(self, size):
        self.pizza.size = size

    def set_crust(self, crust):
        self.pizza.crust = crust

    def set_topping(self, topping):
        self.pizza.toppings.append(topping)
    
    def set_cheesy_crust(self, cheesy_crust):
        self.pizza.cheesy_crust = cheesy_crust

    def get_pizza(self):
        return self.pizza
    
    def get_price(self):
        return self.pizza.get_price()
