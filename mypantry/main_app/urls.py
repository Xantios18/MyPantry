from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view, name='home'),
    path('accounts/signup/', views.signup, name='signup'),
    path('recipes/', views.RecipeList.as_view(), name='recipes'),
    path('recipes/', views.RecipeCreate.as_view(), name='add-recipes'),
    path('recipes/<int:recipe_id>/', views.RecipeDetail.as_view(), name='recipe-details'),
    path('recipes/<int:recipe_id>/edit', views.RecipeDetail.as_view(), name='recipe-details'),
    path('ingredients/', views.IngredientList.as_view(), name='ingredients'),
    # no ingredient detail view necessary. go straight to update view
    path('ingredients/<int:ingredient_id>/update/', views.IngredientUpdate.as_view(), name='ingredient-update'),
]
