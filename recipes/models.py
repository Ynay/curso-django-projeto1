from distutils.command.upload import upload
from email.policy import default
from unicodedata import category

from django.contrib.auth.models import User
from django.db import models
from pyexpat import model


# Create your models here.
# Tabela de Category( categorias )
class Category(models.Model):
    name = models.CharField(max_length=65)

    def __str__(self):
        return self.name


# Tabela de Recipe( Receitas )
class Recipe(models.Model):
    title = models.CharField(max_length=65)
    description = models.CharField(max_length=165)
    slug = models.SlugField()
    preparation_time = models.IntegerField()
    preparation_time_unit = models.CharField(max_length=65)
    servings = models.IntegerField()
    servings_unit = models.CharField(max_length=65)
    preparation_steps = models.TextField()
    preparation_steps_is_html = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)
    cover = models.ImageField(
        upload_to='recipes/covers/%Y/%m/%d/', blank=True, default='')
    # Chave Primaria Pra ligar duas tabela
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True,
        default=None,
    )
    author = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True
    )

    def __str__(self):  # Função usada para retorna nome do titulo na page admin do Django
        return self.title
