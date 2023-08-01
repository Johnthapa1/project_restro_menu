from rest_framework import serializers
from app_menus.models import Menu, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "category_title", "category_code"]
        
class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ("id", "menu_title", "menu_price", "menu_ingredient", "menu_category")
