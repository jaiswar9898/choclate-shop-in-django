from pathlib import Path
from django.contrib import admin
from django.urls import path
from .views import index,sign_up,log,logoutP,HomeView,ProductDetail,add_to_cart,remove_from_cart,remove_single_from_cart,OrderSummaryView, CheckoutView,PaymentView,payment_complete

urlpatterns = [
    path('home',index,name="home"),
    path('accounts/sign_up/',sign_up,name="sign-up"),
    path('accounts/login_up/',log,name="login"),
    path('accounts/logout/',logoutP,name="logoutP"),
    path('list', HomeView.as_view(), name='home'),
    path('product/<slug>/', ProductDetail.as_view(), name='product'),
   
    path('add-to-cart/<slug>/', add_to_cart, name='add_to_cart'),
    path('remove-from-cart/<slug>/', remove_from_cart, name='remove_from_cart'),
    path('remove-single-from-cart/<slug>/',
         remove_single_from_cart, name='remove_single_from_cart'),
    path('order-summary/', OrderSummaryView.as_view(), name='order_summary'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('payment/<payment_option>/', PaymentView.as_view(), name='payment'),
    path('payment-complete', payment_complete, name="payment_complete"),
]