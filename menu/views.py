from django.shortcuts import render
from .models import MenuItems, Category, Cuisine
from django.http import JsonResponse

def get_menu(request):
    menu_items = MenuItems.objects.select_related().all()
    data = []

    for item in menu_items:
        data.append({
            'title': item.title,
            'description': item.description,
            'price': item.price,
            'spicy_level': item.spice_level,
            'category': item.category.type,
            'cuisine': item.cuisine.type
        })

    return JsonResponse(data, safe=False)