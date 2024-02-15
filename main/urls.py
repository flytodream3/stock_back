from django.urls import path, include


app_name = 'api'
urlpatterns = [
    path('users/', include('users.urls')),
    path('warehouse/', include('products.urls')),
    path('partners/', include('partners.urls')),
]
