from django.urls import path
from .views import EateryListView, EateryDetailView, EateryCreateView, EateryUpdateView, EateryDeleteView, UserEateryListView, AdminEateryListView, EateryApproveView
from . import views

urlpatterns = [
    path('', EateryListView.as_view(), name='halalweb-home'),
    path('user/<str:username>', UserEateryListView.as_view(), name='user-eatery'),
    path('approve/', AdminEateryListView.as_view(), name='admin-eatery'),
    path('confirmapprove/<int:pk>/', EateryApproveView.as_view(), name='approve-confirm'),
    path('eatery/<int:pk>/', EateryDetailView.as_view(), name='eatery-detail'),
    path('eatery/<int:pk>/update/', EateryUpdateView.as_view(), name='eatery-update'),
    path('eatery/<int:pk>/delete/', EateryDeleteView.as_view(), name='eatery-delete'),
    path('eatery/new/', EateryCreateView.as_view(), name='eatery-create'),
    path('about/', views.about, name='halalweb-about')
]