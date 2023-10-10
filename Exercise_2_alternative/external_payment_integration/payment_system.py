from handlers.handler import Handler
from payment.payment import Payment

class PaymentSystem:
    def __init__(self, handler: Handler) -> None:
        self.handler = handler

    def pay(self, payment: Payment) -> str:
        return self.handler.handle(payment)