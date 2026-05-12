from django.shortcuts import render, redirect, get_object_or_404
from django.core.exceptions import PermissionDenied
from django.urls import reverse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from .models import Recipe, Ingredient, Variant

# Create your views here.
# def home(request):
#     return render(request, 'home.html')

class Home(LoginView):
    template_name = 'home.html'

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('recipes')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)

class RecipeCreate(LoginRequiredMixin, CreateView):
    model = Recipe
    fields = ['name', 'description']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class RecipeList(ListView):
    model = Recipe

class RecipeDetail(DetailView):
    model = Recipe

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        recipe = self.get_object()
        context['available_ingredients'] = Ingredient.objects.exclude(id__in=recipe.ingredients.values_list('id', flat=True))
        return context

class RecipeUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Recipe
    fields = ['name', 'description']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        recipe = self.get_object()
        return self.request.user == recipe.user

class RecipeDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Recipe
    success_url = '/recipes/'

    def test_func(self):
        recipe = self.get_object()
        return self.request.user == recipe.user

class IngredientCreate(LoginRequiredMixin, CreateView):
    model = Ingredient
    fields = ['name']
    success_url = '/ingredients/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class IngredientList(ListView):
    model = Ingredient

class IngredientUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Ingredient
    fields = ['name']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        ingredient = self.get_object()
        return self.request.user == ingredient.user

class IngredientDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Ingredient
    success_url = '/ingredients/'

    def test_func(self):
        ingredient = self.get_object()
        return self.request.user == ingredient.user
    
@login_required
def recipe_associate_ingredient(request, recipe_id, ingredient_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    if request.user != recipe.user:
        raise PermissionDenied
    Recipe.objects.get(id=recipe_id).ingredients.add(ingredient_id)
    return redirect('recipe-details', pk=recipe_id)

@login_required
def recipe_remove_ingredient(request, recipe_id, ingredient_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    if request.user != recipe.user:
        raise PermissionDenied
    Recipe.objects.get(id=recipe_id).ingredients.remove(ingredient_id)
    return redirect('recipe-details', pk=recipe_id)

class VariantCreate(LoginRequiredMixin, CreateView):
    model = Variant
    fields = ['name', 'description']

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.recipe = get_object_or_404(Recipe, id=self.kwargs['recipe_id'])
        return super().form_valid(form)
    
class VariantDetail(DetailView):
    model = Variant

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        variant = self.get_object()
        excluded_ids = list(variant.ingredients.values_list('id', flat=True)) + list(variant.recipe.ingredients.values_list('id', flat=True))
        context['available_ingredients'] = Ingredient.objects.exclude(id__in=excluded_ids)
        return context
    
class VariantUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Variant
    fields = ['name', 'description']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        variant = self.get_object()
        return self.request.user == variant.user

class VariantDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Variant

    def get_success_url(self):
        return reverse('recipe-details', kwargs={'pk': self.object.recipe.id})

    def test_func(self):
        variant = self.get_object()
        return self.request.user == variant.user

@login_required
def variant_associate_ingredient(request, recipe_id, variant_id, ingredient_id):
    variant = get_object_or_404(Variant, id=variant_id)
    if request.user != variant.user:
        raise PermissionDenied
    Variant.objects.get(id=variant_id).ingredients.add(ingredient_id)
    return redirect('recipe-variant', recipe_id=recipe_id, pk=variant_id)

@login_required
def variant_remove_ingredient(request, recipe_id, variant_id, ingredient_id):
    variant = get_object_or_404(Variant, id=variant_id)
    if request.user != variant.user:
        raise PermissionDenied
    Variant.objects.get(id=variant_id).ingredients.remove(ingredient_id)
    return redirect('recipe-variant', recipe_id=recipe_id, pk=variant_id)