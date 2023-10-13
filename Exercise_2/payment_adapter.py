from payment_method import PaymentMethod
from integration_payment import IntegrationPayment

class PaymentAdapter(PaymentMethod, IntegrationPayment):
    def do_payment(self, usd):
        usd_to_cops = usd * 4000
        self.do_cop_payment(usd_to_cops)