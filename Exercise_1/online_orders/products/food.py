from products.product import Product

class Food(Product):
    """
    Food is one of the concrete products that the factory creates.
    """

    def inventory_check(self) -> str:
        return "Food inventory check"

    def invoice(self) -> str:
        return "Food invoice"

    def notify_client(self) -> str:
        return "Food notify client"
    
    def manage_frozen(self) -> set:
        return "Frozen food management"