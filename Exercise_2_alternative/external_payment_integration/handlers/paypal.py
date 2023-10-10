from handlers.handler import AbstractHandler
from payment.payment import Payment

class PayPalHandler(AbstractHandler):
    def handle(self, payment: Payment) -> str:
        if payment.type == "PayPal":
            print(payment.validate_identity())
            print(payment.validate_funds())
            print(payment.apply_payment())
            return f"PayPal: I paid with {payment.type}"
            
        else:
            return super().handle(payment)