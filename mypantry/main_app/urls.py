from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('accounts/signup/', views.signup, name='signup'),
    path('recipes/', views.RecipeList.as_view(), name='recipes'),
    path('recipes/new/', views.RecipeCreate.as_view(), name='add-recipe'),
    path('recipes/<int:pk>/', views.RecipeDetail.as_view(), name='recipe-details'),
    path('recipes/<int:pk>/edit', views.RecipeUpdate.as_view(), name='edit-recipe'),
    path('recipes/<int:pk>/delete/', views.RecipeDelete.as_view(), name='delete-recipe'),
    path('ingredients/', views.IngredientList.as_view(), name='ingredients'),
    path('ingredients/new/', views.IngredientCreate.as_view(), name='add-ingredient'),
    # no ingredient detail view necessary. go straight to update view
    path('ingredients/<int:pk>/edit/', views.IngredientUpdate.as_view(), name='edit-ingredient'),
    path('ingredients/<int:pk>/delete/', views.IngredientDelete.as_view(), name='delete-ingredient'),
    path('recipes/<int:recipe_id>/associate-ingredient/<int:ingredient_id>', views.recipe_associate_ingredient, name='recipe-associate-ingredient'),
    path('recipes/<int:recipe_id>/remove-ingredient/<int:ingredient_id>/', views.recipe_remove_ingredient, name='recipe-remove-ingredient'),
    path('recipes/<int:recipe_id>/new-variant/', views.VariantCreate.as_view(), name='add-variant'),
    path('recipes/<int:recipe_id>/<int:pk>/', views.VariantDetail.as_view(), name='recipe-variant'),
    path('recipes/<int:recipe_id>/<int:pk>/edit/', views.VariantUpdate.as_view(), name='edit-variant'),
    path('recipes/<int:recipe_id>/<int:pk>/delete/', views.VariantDelete.as_view(), name='delete-variant'),
    path('recipes/<int:recipe_id>/<int:variant_id>/associate-ingredient/<int:ingredient_id>', views.variant_associate_ingredient, name='variant-associate-ingredient'),
    path('recipes/<int:recipe_id>/<int:variant_id>/remove-ingredient/<int:ingredient_id>/', views.variant_remove_ingredient, name='variant-remove-ingredient'),
]
