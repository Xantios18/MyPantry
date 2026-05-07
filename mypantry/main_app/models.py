from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __Str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("ingredient_detail", kwargs={"pk": self.pk})
    
    class Meta:
        ordering = ['name']
    

class Recipe(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    ingredients = models.ManyToManyField(Ingredient)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __Str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("Recipe_detail", kwargs={"recipe_id": self.id})
    
class Variant(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    ingredients = models.ManyToManyField(Ingredient)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __Str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("variant_detail", kwargs={"variant_id": self.id})
    