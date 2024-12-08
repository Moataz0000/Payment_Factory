from django.urls import path
from . import views


app_name = 'payment'


urlpatterns = [
    path('process_payment/<int:payment_id>/', views.process, name='process_payment'),

]