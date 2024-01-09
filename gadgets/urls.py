from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('brand.html', views.brand_view, name='brand'),
    path('category.html', views.category_view, name='category'),
    path('gadget.html', views.gadget_view, name='gadget'),
    path('specification.html', views.specification_view, name='specification'),
    path('user.html', views.user_view, name='user'),
]