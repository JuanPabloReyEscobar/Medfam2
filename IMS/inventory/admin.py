# inventory/admin.py
from django.contrib import admin
from inventory.models import Product, Order, UserProfile

admin.site.site_header = "Inventory Admin"


class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = ["Siglas", "category", "cantidad", "descripcion", "principio_activo", "proveedor", "laboratorio", "codigo", "unidades_paquete", "entrada_unidades"]
    list_filter = ["laboratorio"]
    search_fields = ["nprincipio_activo"]


class OrderAdmin(admin.ModelAdmin):
    model = Order
    list_display = ("product", "created_by", "order_quantity", "date")
    list_filter = ["date"]
    search_fields = ["product"]


class UserProfileAdmin(admin.ModelAdmin):
    model = UserProfile
    list_display = ("user", "physical_address", "mobile", "picture")
    list_filter = ["user"]
    search_fields = ["user"]


admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
