from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('add-to-cart/<int:book_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.view_cart, name='view_cart'),
    path('back/', views.back_to_books, name='back_to_books'),
    path('remove-from-cart/<int:book_id>/', views.remove_from_cart, name='remove_from_cart'),
]

