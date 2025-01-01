from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='home'),  
    path('index/', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('shop/', views.shop, name='shop'),
    path('sale/', views.sale, name='sale'),
    path('help/', views.help, name='help'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('cart/', views.view_cart, name='cart'),
    path('add-to-cart/', views.add_to_cart, name='add_to_cart'),
    path('update-cart/', views.update_cart, name='update_cart'),
    path('terms', views.terms, name='terms'),
    path('accessibility/', views.accessibility, name='accessibility'),
    path('shipping/', views.shipping, name='shipping'),
    path('privacy/', views.privacy, name='privacy'),
    path('refund/', views.refund, name='refund'),
    path('products/', views.product_list, name='products'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
