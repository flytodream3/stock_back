from django.urls import path

from . import views

app_name = 'warehouse'
urlpatterns = [
    path('stockrooms/', views.get_stockrooms, name='stockrooms'),
    path('stockrooms/<room_id>', views.get_stockroom, name='stockroom'),
]
