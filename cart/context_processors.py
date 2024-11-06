from .views import Cart, ProductCartUser
from .forms import QuickOrderForm

def cart(request):
    if request.user.id:
        return {'cart': ProductCartUser(request)}

    return {'cart': Cart(request)}

def quick_order_form(request):
    return {'quick_order_form': QuickOrderForm()}
