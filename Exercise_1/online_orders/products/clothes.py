from products.product import Product

class Clothes(Product):
    """
    Clothes is one of the concrete products that the factory creates.
    """

    def inventory_check(self) -> str:
        return "Clothes inventory check"

    def invoice(self) -> str:
        return "Clothes invoice"

    def notify_client(self) -> str:
        return "Clothes notify client"