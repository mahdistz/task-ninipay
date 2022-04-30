from django.urls import path
from .views import show_products_type1_count_more_than_10, show_products_type2_count_more_than_10, \
    show_products_type3_count_more_than_10, show_products

urlpatterns = [
    path('api/show_products_type1/<str:string>/', show_products_type1_count_more_than_10, name='show_products_type1'),
    path('api/show_products_type2/<str:string>/', show_products_type2_count_more_than_10, name='show_products_type2'),
    path('api/show_products_type3/<str:string>/', show_products_type3_count_more_than_10, name='show_products_type3'),
    path('api/show_products/<int:id>/', show_products, name='show_products_api'),
]
