from django.contrib import admin
from app_menus.models import Category, Menu

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["category_title", "category_code"]
    search_fields=["category_title","category_code"]
    list_filter=["category_title"]

class MenuAdmin(admin.ModelAdmin):
    list_display = ['menu_title', 'menu_price', 'menu_category', 'menu_ingredient', 'menu_created_at']
    search_fields=["menu_title"]
    list_filter=["menu_title","menu_category"]

admin.site.register(Category, CategoryAdmin)
admin.site.register(Menu, MenuAdmin)
