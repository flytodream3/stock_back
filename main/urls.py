from django.urls import path, include


app_name = 'api'
urlpatterns = [
    path('users/', include('users.urls')),
    path('products/', include('products.urls')),
    path('partners/', include('partners.urls')),
]
