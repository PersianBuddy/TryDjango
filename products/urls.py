from django.urls import path
from .views import (
products_list_view,
product_detail_view,
delete_product_view,
create_product_view
)

app_name= 'products'
urlpatterns= [
    path('', products_list_view, name='products_list'),
    path('<int:product_id>/', product_detail_view, name='product_detail'),
    path('create/', create_product_view),
    path('<int:product_id>/delete/', delete_product_view, name='delete_product'),
]