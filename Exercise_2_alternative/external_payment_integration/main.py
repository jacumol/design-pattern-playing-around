from payment_system import PaymentSystem
from handlers.paypal import PayPalHandler
from handlers.credit_card import CreditCardHandler
from handlers.your_soul import YourSoulHandler

from payment.credit_card import CreditCard
from payment.paypal import PayPal
from payment.your_soul import YourSoul

def main():
    credit_card_handler = CreditCardHandler()
    paypal_handler = PayPalHandler()
    your_soul_handler = YourSoulHandler()

    credit_card_handler.set_next(paypal_handler)
    paypal_handler.set_next(your_soul_handler)

    payment_system = PaymentSystem(credit_card_handler)
    
    credit_card = CreditCard("CreditCard", 1000, "USD", "1234-1234-1234-1234", "John Doe", "12/24", "123")
    print(payment_system.pay(credit_card))

    paypal = PayPal("PayPal", 1000, "USD", "johndoe@evilcorp.com", "123")
    print(payment_system.pay(paypal))
    
    your_soul = YourSoul("YourSoul", 1000, "USD", "John Doe")
    print(payment_system.pay(your_soul))

    payment_system_no_credit_card = PaymentSystem(paypal_handler)
    print(payment_system_no_credit_card.pay(credit_card))


if __name__ == "__main__":
    main()  