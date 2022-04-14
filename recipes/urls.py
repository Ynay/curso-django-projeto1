from django.urls import path

from . import views

urlpatterns = [
    path('', views.home),  # Page Home
    path('recipes/<int:id>/', views.recipe),  # Page Recipes
]
