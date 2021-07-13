"""amazon URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from .views import Index, Cart, Order, CartItem, view
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name="main"),
    path('products/', Index.as_view(), name="home"),
    path('login/', views.log_in, name="login"),
    path('logout/', views.log_out, name="logout"),
    path('view/<str:id>', views.view, name="view"),
    path('review/', views.review, name="review"),
    path('cart/', Cart.as_view(), name="cart"),
    path('cartitem/', CartItem.as_view(), name="cartitem"),
    path('order/', Order.as_view(), name='order'),
    path('bookorder/', views.book, name="book"),
    path('profile/', views.profile, name="profile"),
    path('place-order/',views.place, name="place"),
] +static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

