from payment.payment import Payment

class CreditCard(Payment):
    def __init__(self, type: str, amount: float, currency: str, card_number: str, card_holder: str, expiration_date: str, cvv: str) -> None:
        self.type = type
        self.amount = amount
        self.currency = currency
        self.card_number = card_number
        self.card_holder = card_holder
        self.expiration_date = expiration_date
        self.cvv = cvv

    def validate_identity(self) -> str:
        return f"CreditCard: I'll validate the identity of the card holder"

    def validate_funds(self) -> str:
        return f"CreditCard: I'll validate the funds of the card holder"

    def apply_payment(self) -> str:
        return f"CreditCard: I'll apply the payment"