import uuid
import json
from itertools import product

from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404, redirect, reverse, render
from django.http import JsonResponse


from .models import Order, OrderItem
from .forms import OrderForm
from cart.views import Cart, ProductCartUser
from shop.models import Product


#Создание заказа АНОНИМНЫМ пользователем AJAX запросом
@csrf_exempt
def new_order_ajax(request):
    data = json.loads(request.body)
    name = data.get('name')
    last_name = data.get('lastName')
    email = data.get('email')
    phone = data.get('phone')
    delivery = data.get('delivery')
    payment = data.get('payment')

    cart = Cart(request)
    order = Order.objects.create(name=name,
                         last_name=last_name,
                         email=email,
                         phone=phone,
                         delivery=delivery,
                         payment=payment,
                         number=uuid.uuid4(),
                        )
    for item in cart:
        OrderItem.objects.create(order=order, product=item['product'], quantity=item['quantity'])

    # orders = OrderItem.objects.filter(order=order)
    # cart_order = cart.copy()
    cart.clear()

    url = reverse("main")
    json_response = {"status": "ok", "url": url}
    return JsonResponse(json_response)
    # return render(request, template_name='orders/order_create.html', context={'cart_order': cart_order})


# def new_order(request):
#     cart = ProductCartUser(request)
#     order_form = OrderForm(initial={"number": uuid.uuid4(), "user": request.user})
#     pass
#     if order_form.is_valid():
#         pass
