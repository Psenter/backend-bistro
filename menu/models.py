from django.db import models

class Cuisine(models.Model):
    type = models.CharField(max_length=200, null=False, blank=False, unique=True)
    """
    appetizer
    lunch
    dinner
    breakfast
    drinks
    """

    def __str__(self):
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
    price = models.DecimalField(max_digits=4, decimal_places=2, default=0.00)
    spice_level = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=None)
    cuisine = models.ForeignKey(Cuisine, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return f"{self.title} - {self.category} - {self.cuisine}"