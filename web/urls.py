# Create web/urls.py and paste the following
from django.urls import path
from . import views
# from django.views.generic import TemplateView


urlpatterns = [
    path("", views.index, name="index"),
    path("ethnicwear",views.ethnicwear, name='ethnicwear'),
    path("western",views.western, name='western'),
    path("party",views.party, name='party'),
    path("paksthani",views.paksthani, name='paksthani'),
    path("prayer",views.prayer, name='prayer'),
    path('quick-view/<int:product_id>/', views.quick_view, name='quick_view'),

    path("indus",views.indus, name="indus"),
    path("signin", views.signin, name="signin"),
    path("signup", views.signup, name="signup"),
    path("contact", views.contact, name="contact"),
    path('logout/', views.logout_user, name='logout'),
    path('category', views.category, name='category'),
    path('cart', views.cart, name='cart'),
    path('checkout', views.checkout, name='checkout'),
    
    path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/',
         views.item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/',
         views.item_decrement, name='item_decrement'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('cart/cart-detail/',views.cart_detail,name='cart_detail'),
]