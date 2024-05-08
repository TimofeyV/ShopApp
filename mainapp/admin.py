from django.contrib import admin
from .models import User, Product, Order


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone', 'email')
    search_fields = ('id', 'name', 'phone')
    readonly_fields = ('id', 'date_registration')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'quantity')
    search_fields = ('id', 'name', 'quantity')
    readonly_fields = ('id', 'date_add')


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'client', 'total_price')
    search_fields = ('id', 'client', 'products')
    readonly_fields = ('id', 'date_ordered')

    fieldsets = [
        (None, { "fields": ['id', 'client', 'date_ordered'],},),
        ('Данные заказа', { "fields": ['total_price', 'products'], },),
    ]