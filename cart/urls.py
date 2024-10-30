from django.urls import path
from .views import cart_detail, update_cart_by_front


urlpatterns = [
    path('detail/', cart_detail, name="cart_detail"),
    path('update_cart_session/', update_cart_by_front, name="update_cart_session")

]
