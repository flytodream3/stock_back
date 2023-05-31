from django.urls import path

from . import views

app_name = 'partners'
urlpatterns = [
    path('divisions/', views.get_divisions, name='divisions'),
]
