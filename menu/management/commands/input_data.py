import json
import requests
from django.core.management.base import BaseCommand
from menu.models import Category, Cuisine, MenuItems

class Command(BaseCommand):
    help = 'Imports data from JSON file into the database.'

    def handle(self, *args, **kwargs):
        # Read the JSON data from the URL
        url = 'https://www.jsonkeeper.com/b/MDXW'
        response = requests.get(url)
        data = response.json()

        # Process and save the data into the models
        for item in data:
            # Get or create Category
            category_type = item.get('category')
            category, _ = Category.objects.get_or_create(type=category_type)

            # Get the ‘cuisine’ from the JSON data or set a default value
            cuisine_type = item.get('cuisine_type', 'Default Cuisine')
            # Get or create Cuisine
            cuisine, _ = Cuisine.objects.get_or_create(type=cuisine_type)

            # Get the ‘spice_level’ from the JSON data
            spice_level_value = item.get('spicy_level', 0)

            # Create the MenuItem instance
            menu_item = MenuItems.objects.create(
                title=item['title'],
                description=item['description'],
                price=item['price'],
                spice_level=spice_level_value,
                category=category,  # Use category instead of category_id
                cuisine=cuisine,    # Use cuisine instead of cuisine_id
            )
            self.stdout.write(self.style.SUCCESS(f'Successfully added {menu_item}'))