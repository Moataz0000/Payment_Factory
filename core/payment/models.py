from django.db import models




class Payment(models.Model):
    CREDIT_CARD = 'credit_card'
    PAYPAL      = 'paypal'
    APPLE_PAY   = 'apple_pay'
    
    
    PAYMENT_METHODS = [
        (CREDIT_CARD, 'Credit Card'),
        (PAYPAL, 'PayPal'),
        (APPLE_PAY, 'Apple Pay')
    ]

    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHODS)
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self) -> str:
        return str(f'{self.amount} ')