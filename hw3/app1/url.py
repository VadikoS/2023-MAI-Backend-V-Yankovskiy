from django.urls import path

from . import views

urlpatterns = [
    path('', views.main_view, name='main_view'),
    path('profiles/', views.get_profiles, name='all_profiles'),
    path('profile/<int:profile_id>/', views.get_profile, name='specific_profile'),
    path('profiles/', views.create_profile, name='create_profile'),

    path('products/', views.get_products, name='all_products'),
    path('products/create/', views.create_product, name='create_product'),
    path('products/<int:product_id>/', views.get_product, name='specific_product'),

    path('orders/', views.get_orders, name='all_orders'),
    path('orders/create/', views.create_order, name='create_order'),
]