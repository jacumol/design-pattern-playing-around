from payment.payment import Payment

class PayPal(Payment):
    def __init__(self, type: str, amount: float, currency: str, email: str, password: str) -> None:
        self.type = type
        self.amount = amount
        self.currency = currency
        self.email = email
        self.password = password

    def validate_identity(self) -> str:
        return f"PayPal: I'll validate the identity of the user"

    def validate_funds(self) -> str:
        return f"PayPal: I'll validate the funds of the user"

    def apply_payment(self) -> str:
        return f"PayPal: I'll apply the payment"