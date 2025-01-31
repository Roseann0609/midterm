from django.urls import path
from .import views
from .views import (HomePageView, PaymentView, ProductListView, ProductDetailView, 
                    ProductCreateView, ProductUpdateView, ProductDeleteView)

urlpatterns = [
    path('home/', HomePageView.as_view(), name='home'),
    path('product/', ProductListView.as_view(), name='product'),
    path('product/<int:pk>', ProductDetailView.as_view(), name='product_detail'),
    path('product/create', ProductCreateView.as_view(), name='product_create'),
    path('product/<int:pk>/edit', ProductUpdateView.as_view(), name='product_update'),
    path('product/<int:pk>/delete', ProductDeleteView.as_view(), name='product_delete'),
    path('review/', views.review_page, name='review'),
    path('contact/', views.contact_page, name='contact'),
    path('', views.LoginView.as_view(), name='login'),
    path('signup/', views.SignupView.as_view(), name='signup'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('payment/', PaymentView.as_view(), name='payment'),
    

]
