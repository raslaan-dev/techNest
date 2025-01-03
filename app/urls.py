from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='home'),  
    path('index/', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('shop/', views.shop, name='shop'),
    path('sale/', views.sale, name='sale'),
    path('help/', views.help, name='help'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('cart/', views.cart_view, name='cart'),
    path('add-to-cart/', views.add_to_cart, name='add_to_cart'),
    path('update-cart/', views.update_cart, name='update_cart'),
    path('terms', views.terms, name='terms'),
    path('accessibility/', views.accessibility, name='accessibility'),
    path('shipping/', views.shipping, name='shipping'),
    path('privacy/', views.privacy, name='privacy'),
    path('refund/', views.refund, name='refund'),
    path('products/', views.product_list, name='products'),
    path('cart/sidepanel/', views.cart_sidepanel, name='cart_sidepanel'),
    path('product-management/', views.product_management, name='product_management'),
    path('edit-product/<int:product_id>/', views.edit_product, name='edit_product'),
    path('delete-product/<int:product_id>/', views.delete_product, name='delete_product'),
    path('checkout/', views.checkout, name='checkout'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('cart/remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('profile/', views.profile_view, name='profile'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
