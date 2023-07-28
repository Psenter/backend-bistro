import json
import requests
from django.core.management.base import BaseCommand
from menu.models import Category, Cuisine, MenuItems


class Command(BaseCommand):

    #takes the JSON from the api

    def handle(self, *args, **kwargs):
        url = 'https://www.jsonkeeper.com/b/MDXW'
        response = requests.get(url)
        data = response.json()

        #retrieves all the data from api
        #will create new objects if it does not exsist
        for item in data:
            category_type = item.get('category')
            category, _ = Category.objects.get_or_create(type=category_type)

            cuisine_type = item.get('cuisine_type', 'Default Cuisine')
            cuisine, _ = Cuisine.objects.get_or_create(type=cuisine_type)

            spice_level_value = item.get('spicy_level', 0)

            menu_item = MenuItems.objects.create(
                title=item['title'],
                description=item['description'],
                price=item['price'],
                spice_level=spice_level_value,
                category=category,
                cuisine=cuisine,
            )

            #lets user know that everything was added successfully
            self.stdout.write(self.style.SUCCESS(f'Successfully added {menu_item}'))