from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),  
    path('index/', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('shop/', views.shop, name='shop'),
    path('sale/', views.sale, name='sale'),
    path('help/', views.help, name='help'),
]
