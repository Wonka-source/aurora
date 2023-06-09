from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Product
from .forms import ProductForm


def all_products(request):
    """
    A view to show all products, including sorting and search queries
    """

    products = Product.objects.all().order_by('-price')

    context = {
        'products': products,
    }

    return render(request, 'shop/shop.html', context)


def product_detail(request, product_id):
    """
    A view to show individual product details
    """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'shop/product_detail.html', context)


@login_required
def add_product(request):
    """
    Add a product to the store
    """
    if not request.user.is_staff:
        messages.error(request, 'Sorry, you are not authorized to do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(
                request, 'Failed to add product. \
                    Please ensure the form is valid.')
    else:
        form = ProductForm()

    template = 'shop/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """
    Edit a product in the store
    """
    if not request.user.is_staff:
        messages.error(request, 'Sorry, you are not authorized to do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(
                request, 'Failed to update product. \
                    Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'shop/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """
    Delete a product from the store
    """
    if not request.user.is_staff:
        messages.error(request, 'Sorry, you are not authorized to do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)

    if request.method == 'POST':
        product.delete()

        cart = request.session.get('cart', {})
        for item_id in list(cart.keys()):
            if int(item_id) == product_id:
                del cart[item_id]
        request.session['cart'] = cart

        messages.success(request, 'Product deleted!')
        return redirect(reverse('shop'))
    else:
        messages.info(request, f'Are you sure you want to delete {product.name}?')

    template = 'shop/delete_product.html'
    context = {'product': product}
    return render(request, template, context)
