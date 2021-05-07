from django.urls import path, include
from .views import Home, StockListView, fav, register

urlpatterns = [
    path('', Home, name='home' ),
    path('all/', StockListView.as_view(), name='stocks'),
    path('fav/<str:id>/', fav, name='favourite'),
    path('register/', register, name='registration')
]