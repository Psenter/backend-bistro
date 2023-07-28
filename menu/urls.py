#imports what i need into the file
from django.urls import path
#imports views into the file
from . import views

urlpatterns = [
    #defines the path for menu/
    path('menu/', views.get_menu, name='get_menu'),
]