class Pizza:
    def __init__(self):
        self.size = None
        self.crust = None
        self.toppings = []
        self.cheesy_crust = False

    def __str__(self):
        return f"""
            {self.crust} {self.size} pizza, with {", ".join(self.toppings)}.
            Cheesy crust: {"Yes." if self.cheesy_crust else "No."}
        """

    def get_price(self):
        price = 0

        if "classic" == self.crust.lower():
            price += 50
        
        if "crust" == self.crust.lower():
            price += 70

        if self.cheesy_crust:
            price += 50

        if "large" == self.size.lower():
            price += 100
        
        if "medium" == self.size.lower():
            price += 100
        
        if "small" == self.size.lower():
            price += 100
        
        price += len(self.toppings) * 30

        return f"""
            Total: {price}
        """
