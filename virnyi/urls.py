from django.urls import path
from virnyi import views

urlpatterns = [
    path('', views.home, name='home'),
    path('page1/', views.page1, name='page1'),
    path('page2/', views.page2, name='page2'),
    path('page3/', views.page3, name='page3'),
    path('page4/', views.page4, name='page4'),
    path('menu/', views.category_list, name='category_list'),  # додано URL для меню
    path('category/<int:category_id>/', views.category_detail, name='category_detail'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
]
