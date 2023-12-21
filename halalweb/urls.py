from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='halalweb-home'),
    path('about/', views.about, name='halalweb-about')
]