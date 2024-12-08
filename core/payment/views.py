from django.shortcuts import render
from django.http import JsonResponse
from .models import Payment
from .factories import PaymentFactory



def process(request, payment_id):
    
    try:
        payment = Payment.objects.get(id=payment_id)
        processor = PaymentFactory.get_payment_processor(payment.payment_method)
        result = processor.process_payment(payment.amount)
        return JsonResponse({'status': 'success', 'message': result})

    except Payment.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'Payment not found'})
   
    except ValueError as e:
        return JsonResponse({'status': 'error', 'message': str(e)})