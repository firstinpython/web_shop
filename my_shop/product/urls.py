from django.urls import path
from .views import products, basket_add, basket


urlpatterns = [
    path("",products, name="products"),
    path("basket_add/<int:product_id>", basket_add, name="basket_add"),
    path("basket", basket, name="basket")
]