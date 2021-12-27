from django.urls import path
from .views import *

urlpatterns = [
    path('prices/<str:stock_ids>', view_stock_price, name='stock-prices'),
    path('price/<str:stock_id>', view_single_price, name='stock-price'),
]