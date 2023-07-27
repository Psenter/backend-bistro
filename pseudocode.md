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

Ref: Menu_items.cuisine_id > Cuisine.id // many-to-one

Ref: Menu_items.category_id > Category.id
```

# Endpoints:
```
-/menu_items
-/breakfast
-/lunch
-/dinner
-/appetizers
```