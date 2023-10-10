from handlers.handler import AbstractHandler
from payment.payment import Payment

class CreditCardHandler(AbstractHandler):
    def handle(self, payment: Payment) -> str:
        if payment.type == "CreditCard":
            print(payment.validate_identity())
            print(payment.validate_funds())
            print(payment.apply_payment())
            return f"CreditCard: I paid with {payment.type}"
            
        else:
            return super().handle(payment)