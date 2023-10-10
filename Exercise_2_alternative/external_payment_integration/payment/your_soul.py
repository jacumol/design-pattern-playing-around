from payment.payment import Payment

class YourSoul(Payment):
    def __init__(self, type: str, amount: float, currency: str, soul: str) -> None:
        self.type = type
        self.amount = amount
        self.currency = currency
        self.soul = soul

    def validate_identity(self) -> str:
        return f"YourSoul: I'll validate the identity of the soul"

    def validate_funds(self) -> str:
        return f"YourSoul: I'll validate the funds of the soul"

    def apply_payment(self) -> str:
        return f"YourSoul: I'll apply the payment"