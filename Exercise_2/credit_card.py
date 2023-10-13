from payment_method import PaymentMethod

class CreditCard(PaymentMethod):
    def do_payment(self, usd):
        print(f"Successful payment, {usd} USD!")