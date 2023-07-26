# MoSCoW

## Must have:
* Store menu data in SQL database
* Menu_items table must have:
    * ID
    * name
    * price
    * spice level
    * foreign key to category table
    * foreign key to cuisin table
* Category table must have:
    * ID
    * type (what category of food, i.e.: appetizer, lunch, dinner)
* Cuisine table must have:
    * ID
    * type (what cuisine type, i.e.: american, thai, chinese)
* Connect to React API for the restaurant

## Should have:
* Way to display tables/all data

## Could have:
Connections to different locations to get different menu items

## Won't have:
* Drinks of any kind (you can swallow your own spit)

# Questions:
How do I connect the API to the tables?
How do I add all the API data to the tables?
How do the foreign keys work?

# Notes:
Look back at heros table to see how to get IDs to increment

# Database schema
```
-3 tables are needed
    -Menu_items
    -Category
    -Cuisine
    (more can be added later on)

-Menu_items:
    -ID
    -name
    -spice_level
    -price
    -description
    -category_id
    -cuisine_id

-Category:
    -ID
    -type

-Cuisine:
    -ID
    -type

-------------
*From dbdiagram*

Table Menu_items {
  id int [primary key]
  name varchar
  spice_level int
  price int
  description varchar
  cuisine_id int
  category_id int
}

Table Cuisine {
  id int [primary key]
  type varchar
}

Table Category {
  id int [primary key]
  type varchar
}

-table bridges

Ref: Menu_items.cuisine_id > Cuisine.id // many-to-one

Ref: Menu_items.category_id > Category.id
```

# Class based structure
```
class GetMenuItem(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=4)
    spicy_level = models.IntegerField()
    category = models.ForeignKey()
    cuisine = models.ForeignKey()

    def __str__(self):
        return self.text

class GetCategory(models.Model):
    type = models.CharField(max_length = 100)

    def __str__(self):
        return self.text

class GetCuisine(models.Model):
    type = models.CharField(max_length = 100)

    def __str__(self):
        return self.text
```

# Python functions
```
def all_menu_items()
    menu_items = Menu_items.object.all()
    for item in menu_items:
        data.append({
            "id": item.id,
            "title": item.title,
            "description": item.description,
            "price": item.price,
            "spice_level": item.spice_level,
            "category": item.category_id,
            "cuisine": item.cuisine_id,
        })

def categories()
    category_type = Category.object.all()
    for item in category_type:
        data.append({
            "id": item.id
            "type": item.type
        })

def categories()
    cuisine_type = Cuisine.object.all()
    for item in cuisine_type:
        data.append({
            "id": item.id
            "type": item.type
        })
```

# Endpoints:
```
-/menu_items
-/breakfast
-/lunch
-/dinner
-/appetizers
```