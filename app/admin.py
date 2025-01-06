from django.contrib import admin
from .models import Category, Product, Order, OrderItem, Review, ShoppingCart, CartItem, Payment

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Review)
admin.site.register(ShoppingCart)
admin.site.register(CartItem)
admin.site.register(Payment)


