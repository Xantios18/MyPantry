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
]
