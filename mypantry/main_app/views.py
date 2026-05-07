from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from .models import Recipe, Ingredient

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
            return redirect('cat-index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)

class RecipeList(ListView):
    model = Recipe

class RecipeDetail(DetailView):
    model = Recipe

class IngredientList(ListView):
    model = Ingredient

class IngredientUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Ingredient
    fields = ['name']

    def test_func(self):
        ingredient = self.get_object()
        return self.request.user.id == ingredient.user.id

