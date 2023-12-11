from django.contrib import admin
from .models import Product, Order, Client
# Register your models here.

@admin.action(description='Обнулить количество продуктов')
def update_count(modeladmin, request, queryset):
    queryset.update(count=0)

class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email',)
    list_filter = ('name',)
    search_fields = ('name', 'email')
    readonly_fields = ('email', 'date_register')
    fieldsets = [
        (
            'About',
            {
                'classes': ['wide'],
                'fields': ['name','email','phone','adress'],
            },
        ),      
         (
            'Date',
            {
                'classes': ['wide'],
                'fields': ['date_register'],
            },
        ),      
    ]


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'count',)
    list_filter = ('name','price',)
    search_fields = ('name',)
    readonly_fields = ('image', 'date_update')
    fieldsets = [
        (
            'About',
            {
                'classes': ['wide'],
                'fields': ['name','price','count','about'],
            },
        ),      
         (
            'Advanced',
            {
                'classes': ['wide'],
                'fields': ['date_update', 'image'],
            },
        ),      
    ]
    actions = [update_count]


class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer', 'total_price', 'count')
    list_filter = ('total_price',)
    search_fields = ('customer',)
    readonly_fields = ('customer', 'products', 'total_price', 'count')


admin.site.register(Client, ClientAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
