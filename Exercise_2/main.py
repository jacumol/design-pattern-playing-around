from paypal import PayPal
from credit_card import CreditCard
from payment_adapter import PaymentAdapter

from digital_platform import DigitalPlatform

def main():
    paypal_method = PayPal()
    credit_card_payment = CreditCard()
    new_method_payment = PaymentAdapter()

    platform = DigitalPlatform(credit_card_payment)
    print("\nUSD Credit card payment: ")
    platform.finish_transaction(59)

    print("\nCOP platform payment: ")
    platform = DigitalPlatform(new_method_payment)
    platform.finish_transaction(73)

    print("\nUSD PayPal payment: ")
    platform = DigitalPlatform(paypal_method)
    platform.finish_transaction(87)

if __name__ == "__main__":
    main()