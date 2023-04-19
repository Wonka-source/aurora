from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm


def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "There's nothing in your cart at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_live_51Mxy0rCv1VUOGFUZY1QyUtHkFPKLsaTeR9YLDTQy9ETvulMdptrGQqPWz600g3rOWCtXdMnHFjl0NYopc8XjAqIY00d1emRtkA',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)