import stripe
from django.shortcuts import render, redirect
from decouple import config

stripe.api_key = config("STRIPE_SECRET_KEY")

def checkout_view(request):
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                'currency': 'usd',
                'unit_amount': 4900,
                'product_data': {'name': 'Starter Plan'},
            },
            'quantity': 1,
        }],
        mode='subscription',
        success_url='http://127.0.0.1:8000/payments/success/',
        cancel_url='http://127.0.0.1:8000/payments/cancel/',
    )
    return redirect(session.url, code=303)

def success_view(request):
    return render(request, 'payments/success.html')

def cancel_view(request):
    return render(request, 'payments/cancel.html')
