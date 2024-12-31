from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),  
    path('index/', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('shop/', views.shop, name='shop'),
    path('sale/', views.sale, name='sale'),
    path('help/', views.help, name='help'),
    path('login/', views.login, name='login'),
    path('cart/', views.cart, name='cart'),
    path('terms', views.terms, name='terms'),
    path('accessibility/', views.accessibility, name='accessibility'),
    path('shipping/', views.shipping, name='shipping'),
    path('privacy/', views.privacy, name='privacy'),
    path('refund/', views.refund, name='refund'),
    
]
