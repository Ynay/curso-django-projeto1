from django.urls import path

from . import views

app_name = 'recipes'

urlpatterns = [
    path('', views.home, name="home"),  # Page Home
    path('recipes/<int:id>/', views.recipe, name="recipe"),  # Page Recipes

]
