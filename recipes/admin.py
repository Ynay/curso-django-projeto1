from django.contrib import admin
from .models import Category, Recipe

# Registar a tabela de category no admin do Django
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin): #Usada para Registrar A tabela na Page Admin do Django
    ...
# Registrar a tabela de recipe no admin do Django
@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):#Usada para Registrar A tabela na Page Admin do Django
    ...




