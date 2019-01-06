from django.shortcuts import render
from django.views import generic
from django.core.paginator import Paginator
from django.conf import settings
import stripe
import decimal

stripe.api_key = settings.STRIPE_SECRET_KEY

from .models import Product
# Create your views here.
class ProductListView(generic.ListView):
    model = Product
    paginate_by = 3
    def get_context_data(self, **kwargs): # new
        context = super().get_context_data(**kwargs)
        context['key'] = settings.STRIPE_PUBLISHABLE_KEY
        return context

def charge(request):
    if request.method == 'POST':
        id = request.POST['id']
        product = Product.objects.get(id=id)
        price = product.price * 100
        price = round(decimal.Decimal(price))
        charge = stripe.Charge.create(
            amount=price,
            currency='usd',
            description='A Django charge',
            source=request.POST['stripeToken']
        )
        product.available = False
        product.address = request.POST['stripeShippingAddressLine1']
        product.email = request.POST['stripeEmail']
        product.save()
    return render(request, 'store/charge.html')
