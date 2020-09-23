"""adeep_handicraft URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from store import views
from users import views as user_views
from django.contrib.auth import views as authentication_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('search', views.search, name='search'),
    path('category/<slug:cat_slug>',
         views.category_list, name='category_list'),
    path('register/', user_views.register, name='register'),
    # login
    path('login/', authentication_views.LoginView.as_view(
        template_name='users/login.html'), name='login'),
    # logout
    path('logout/', user_views.logout_view, name='logout'),
    # profile
    path('profile/', user_views.profilepage, name='profile'),
    # details
    path('detail/<int:id>/', views.detail, name='detail'),
    # add to cart
    path('update_item/', views.updateItem, name='update_item'),
    # cart
    path('cart/', views.cart, name='cart'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('update_wishlist/', views.updateWishlist, name='update_wishlist'),


]
