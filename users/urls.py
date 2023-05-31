from django.urls import path

from . import views

app_name = 'users'
urlpatterns = [
    path('login/', views.MyTokenObtainPairView.as_view(), name='token_login'),
]
