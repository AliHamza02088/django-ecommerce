from django.shortcuts import render , get_object_or_404
from .models import Product
0

# Create your views here.
def index_view(request):
    trending_items = Product.objects.all()[:6]
    mobile_phones = Product.objects.filter(category__category_id__name="Mobile Phones")
    tablets = Product.objects.filter(category__category_id__name="Tablet")
    return render(request, "store/index.html", {"trending_items": trending_items , "mobile_phones":mobile_phones , "tablets":tablets})

def checkout_cart_view(request):
    return render(request , "store/checkout_cart.html")

def checkout_complete_view(request):
    return render(request, "store/checkout_complete.html")


def checkout_info_view(request):
    return render(request, "store/checkout_info.html")


def checkout_payment_view(request):
    return render(request, "store/checkout_payment.html")


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


def product_detail_view(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, "store/product_detail.html" , {"product":product})


def product_view(request):
    all_products = Product.objects.all()
    return render(request, "store/product.html" , {"all_products":all_products})


def search_results_view(request):
    return render(request, "store/search_results.html")


def about_us_view(request):
    return render(request, "store/about_us.html")
