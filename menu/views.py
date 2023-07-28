from django.shortcuts import render
from .models import MenuItems
from django.http import JsonResponse

#defines get_menu function
def get_menu(request):
    #gets all the MenuItems objects on the table
    menu_items = MenuItems.objects.select_related().all()
    #makes an empty list
    data = []

    #for loop to go through all the objects gotten from the table
    for item in menu_items:
        #appends all the items to the data list
        data.append({
            'title': item.title,
            'description': item.description,
            'price': item.price,
            'spicy_level': item.spice_level,
            'category': item.category.type,
            'cuisine': item.cuisine.type
        })

    #converts the data to JSON
    return JsonResponse(data, safe=False)