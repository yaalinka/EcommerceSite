from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', store, name='store'),
    path('cart/', cart, name='cart'),
    path('product/<str:pk>', view_product, name='product'),
    path('checkout/', checkout, name='checkout'),
    path('update_item/', updateItem, name='update_item'),
    path('process_order/', processOrder, name='process_order'),
    path('logout/', LogoutView.as_view(next_page='store'), name='logout'),
]