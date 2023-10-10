class Director:
    def __init__(self, builder):
        self.builder = builder

    def bake_pizza(self):
        self.builder.set_size("Large")
        self.builder.set_crust("Classic")
        self.builder.set_topping("cheese")
        self.builder.set_cheesy_crust(True)
        self.builder.set_topping("pepperoni")
        self.builder.set_topping("pineapple")
