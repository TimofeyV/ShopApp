from django.contrib import admin
from .models import User, Product, Order


@admin.action(description='Сбросить количество товаров')
def reset_quantity(modeladmin, request, queryser):
    queryser.update(quantity = 0)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone', 'email')
    list_filter = ('name', 'phone')
    search_fields = ('id', 'name', 'phone')
    readonly_fields = ('id', 'date_registration')
    search_fields = ('name',)
    search_help_text = 'Поиск по логину'
    ordering = ('id', )

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'quantity')
    list_filter = ('name','price', 'quantity')
    search_fields = ('id', 'name', 'quantity')
    readonly_fields = ('id', 'date_add')
    search_fields = ('name',)
    search_help_text = 'Поиск по названию товара'
    ordering = ('id', )
    actions = [reset_quantity]


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'client', 'total_price')
    list_filter = ('client',)
    search_fields = ('id', 'client', 'products')
    readonly_fields = ('id', 'date_ordered')
    search_fields = ('client',)
    search_help_text = 'Поиск по клиенту'
    ordering = ('-date_ordered', )

    fieldsets = [
        (None, { "fields": ['id', 'client', 'date_ordered'],},),
        ('Данные заказа', { "fields": ['total_price', 'products'], },),
    ]