#imports what i need into models
from django.db import models

#defines the class 
#'models.Model' is the base class for all django models
class Cuisine(models.Model):
    #defines my field
    #charfield stands for character field(string)
    #max_length is set to 200
    #null=False means the field cannot be empty
    #blank=False means the field cannot be blank
    #unique=True means all the types must be unique and nothing will repeat
    type = models.CharField(max_length=200, null=False, blank=False, unique=True)
    """
    appetizer
    lunch
    dinner
    breakfast
    drinks
    """
    #converts objects to strings
    def __str__(self):
        #returns string object
        return self.type

class Category(models.Model):
    type = models.CharField(max_length=200, null=False, blank=False, unique=True)
    """
    american
    thai
    italian
    mexican
    japanese
    southern
    british
    vietnamese
    chinese
    french
    indian
    mediterranean
    russian
    middle_eastern
    asian
    international
    """

    def __str__(self):
        return self.type

class MenuItems(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False, default="")
    description = models.CharField(max_length=200, null=False, blank=False, default="")
    #decimal field sets the object to be a decimal number
    #max digits are 4
    #max decimal places is 2
    price = models.DecimalField(max_digits=4, decimal_places=2, default=0.00)
    #integer field makes the object a number
    #sets default to 0
    spice_level = models.IntegerField(default=0)
    #establishes the foreginkey relationship between the tables
    #on_delete=models.CASCADE: when an item is deleted all the menu items connected to the cuisine/category will also be deleted
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=None)
    cuisine = models.ForeignKey(Cuisine, on_delete=models.CASCADE, default=None)

    #defines string method for the class
    def __str__(self):
        #returns title, category, and cuisine as a string
        return f"{self.title} - {self.category} - {self.cuisine}"