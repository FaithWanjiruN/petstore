from django.urls import path
from . import views
from .views import add_to_cart

urlpatterns = [
        #Leave as empty string for base url
    path('', views.home, name="home"),
    path('store/', views.store, name="store"),
	path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),
    path('signup/',views.signup,name='signup'),
    path('login/',views.user_login,name='login'),
    path('logout/',views.logout,name='logout'),
    
    path('add_to_cart/<int:product_id>/', add_to_cart, name='add_to_cart'),

	path('update_item/', views.updateItem, name="update_item"),
	path('process_order/', views.processOrder, name="process_order"),

]