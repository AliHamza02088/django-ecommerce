from datetime import datetime
from django.shortcuts import redirect, render , get_object_or_404
from .models import Product, cart , Address
from django.contrib.auth.decorators import login_required
from django.conf import settings
import stripe
# Create your views here.
stripe.api_key = settings.STRIPE_SECRET_KEY

@login_required
def index_view(request):
    trending_items = Product.objects.all()[:6]
    mobile_phones = Product.objects.filter(category__category_id__name="Mobile Phones")
    tablets = Product.objects.filter(category__category_id__name="Tablet")
    carts = cart.objects.all()
    return render(request, "store/index.html", {"trending_items": trending_items , "mobile_phones":mobile_phones , "tablets":tablets , "carts":carts})

@login_required
def checkout_cart_view(request):
    carts = cart.objects.all()
    cart_quantity = sum(cart.quantity * cart.total for cart in carts)
    cart_subtotal = sum(cart.grand_total for cart in carts)
    return render(request, 'store/checkout_cart.html',{'carts':carts , 'cart_subtotal':cart_subtotal , "cart_quantity":cart_quantity})


def checkout_complete_view(request):
    carts = cart.objects.all()
    cart_quantity = sum(cart.quantity * cart.total for cart in carts)
    cart_subtotal = sum(cart.grand_total for cart in carts)
    return render(request, "store/checkout_complete.html" , {'carts':carts , 'cart_subtotal':cart_subtotal , "cart_quantity":cart_quantity})

@login_required
def checkout_info_view(request):
    if request.method == 'POST':
        # Extract data from POST request
        first_name = request.POST.get('first_name') or None
        last_name = request.POST.get('last_name') or None
        address = request.POST['address']
        area_code = int(request.POST['area_code'])
        phone_number = int(request.POST['phone_number'])
        zip_code = int(request.POST['zip_code'])
        company = request.POST.get('company') or None
        business = 'business' in request.POST  # Check if checkbox was checked

        # Create and save new Address instance
        Address.objects.create(
            first_name=first_name,
            last_name=last_name,
            address=address,
            area_code=area_code,
            phone_number=phone_number,
            zip_code=zip_code,
            company=company,
            business=business
        )
        return redirect("checkout_payment")
    return render(request, "store/checkout_info.html")
        


def contact_us_view(request):
    return render(request, "store/contact_us.html")


def faq_view(request):
    return render(request, "store/faq.html")


def index_fixed_view(request):
    return render(request, "store/index_fixed_header.html")


def index_inverse_header_view(request):
    return render(request, "store/index_inverse_header.html")


def my_account_view(request):
    return render(request, "store/my_account.html")

@login_required
def product_detail_view(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    carts = cart.objects.all()
    all_products = Product.objects.all()[:6]
    
    if request.method == "POST":
        product_id = request.POST.get("product_id")
        product = get_object_or_404(Product, id=product_id)
        
        cart_item, created = cart.objects.get_or_create(
            user_id=request.user,
            pro_id=product,
            )
        
        if not created:
            cart_item.quantity += 1
            
        cart_item.total = product.price
        cart_item.grand_total = cart_item.total * cart_item.quantity
        cart_item.save()
            
    return render(request, "store/product_detail.html" , {"product":product , "all_products":all_products , "carts":carts})


def product_view(request):
    all_products = Product.objects.all()
    return render(request, "store/product.html" , {"all_products":all_products})


def search_results_view(request):
    return render(request, "store/search_results.html")


def about_us_view(request):
    return render(request, "store/about_us.html")


@login_required
def checkout_payment_view(request):
    if request.method == 'POST':
        cardholder_name = request.POST.get('cardholder_name')
        card_number = request.POST.get('card_number').replace(' ', '')
        exp_month = request.POST.get('exp_month')
        exp_year = request.POST.get('exp_year')
        csc = request.POST.get('csc')

        total_amount = request.session.get('total_amount', 0) 
        if total_amount <= 0:
            return render(request, "store/checkout_payment.html", {'error': 'Invalid payment amount'})

        try:
            payment_method = stripe.PaymentMethod.create(
                type='card',
                card={
                    'cardholder_name':cardholder_name,
                    'number': card_number,
                    'exp_month': exp_month,
                    'exp_year': exp_year,
                    'cvc': csc,
                },
            )

            payment_intent = stripe.PaymentIntent.create(
                amount=int(total_amount * 100),
                currency='usd',
                payment_method=payment_method.id,
                confirm=True,
            )

            if payment_intent.status == 'succeeded':
                return redirect('payment_success')
            else:
                return render(request, "store/checkout_payment.html", {'error': 'Payment failed'})

        except stripe.error.StripeError as e:
            return render(request, "store/checkout_payment.html", {'error': str(e)})
        except Exception as e:
            return render(request, "store/checkout_payment.html", {'error': 'An error occurred'})

    return render(request, "store/checkout_payment.html", {
        'stripe_public_key': settings.STRIPE_PUBLIC_KEY
    })