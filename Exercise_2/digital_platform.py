class DigitalPlatform():
    def __init__(self, payment_method):
        self.payment_method = payment_method

    def finish_transaction(self, usd):
        self.payment_method.do_payment(usd)