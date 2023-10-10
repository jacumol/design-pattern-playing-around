from products.product import Product

class Electronic(Product):
    """
    Electronic is one of the concrete products that the factory creates.
    """

    def inventory_check(self) -> str:
        return "Electronic inventory check"

    def invoice(self) -> str:
        return "Electronic invoice"

    def notify_client(self) -> str:
        return "Electronic notify client"