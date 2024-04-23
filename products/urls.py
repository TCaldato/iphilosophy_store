
from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('add/', views.add_product, name='add_product'),
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path('delete/<int:product_id>/', views.delete_product, name='delete_product'),
    path('<int:product_id>/add_review/', views.add_review, name='add_review'),
    path('<int:product_id>/edit_review/<int:review_id>/', views.edit_review, name='edit_review'),
    path('<int:product_id>/delete_review/<int:review_id>/', views.delete_review, name='delete_review'),
    path('wishlist/', views.view_wishlist, name='wishlist'),
    path('add_to_wishlist/<int:product_id>/', views.add_to_wishlist, name='add_to_wishlist'),
    path('remove_from_wishlist/<int:product_id>/', views.remove_from_wishlist, name='remove_from_wishlist'),
]
