import json
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404, redirect, reverse
from django.http import JsonResponse

from .models import Order, OrderItem
from cart.views import Cart
from shop.models import Product


@csrf_exempt
def new_order(request):
    data = json.loads(request.body)
    name = data.get('name')
    last_name = data.get('lastName')
    email = data.get('email')
    phone = data.get('phone')
    delivery = data.get('delivery')
    payment = data.get('payment')

    cart = Cart(request)

    cart.clear()
    url = reverse("main")
    json_response = {"status": "ok", "url": url}
    return JsonResponse(json_response)