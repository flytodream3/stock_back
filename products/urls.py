from django.urls import path

from . import views

app_name = 'products'
urlpatterns = [
    path('categories/', views.get_categories, name='categories'),
    path('category/<cat_id>/', views.get_category, name='category'),
    path('products/', views.get_products, name='products'),
    path('product/<prod_id>/', views.get_product, name='product'),
]
