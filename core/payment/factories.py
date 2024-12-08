
class CreditCardPayment:
    def process_payment(self, amount):
        return f'Processing credit card payment of ${amount}'
    
    
    
class PayPalPayment:
    def process_payment(self, amount):
        return f'Processing Paypal payment of ${amount}'
    
    

class ApplePayPayment:
    def process_payment(self, amount):
        return f'Processing ApplePay payment of ${amount}'
    
    


class PaymentFactory:
    
    @staticmethod
    def get_payment_processor(payment_method):
        
        if payment_method == 'credit_card':
            return CreditCardPayment()
        
        elif payment_method == 'paypal':
            return PayPalPayment()
        
        elif payment_method == 'apple_pay':
            return ApplePayPayment()
        
        else:
            raise ValueError('Invalid payment method')