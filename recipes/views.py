from django.shortcuts import render,  redirect, get_object_or_404
from django.http import HttpResponse
from .models import Customer
from .forms import RecipeForm
import requests

RECIPE_BASE_URL = "https://60f5adf918254c00176dffc8.mockapi.io/api/v1/recipes/"


def home(request):
    if request.method == "POST":
        form = RecipeForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            email = form.cleaned_data.get('email')
            child_first_name = form.cleaned_data.get(
                'child_first_name')
            child_last_name = form.cleaned_data.get('child_last_name')
            allergies = form.cleaned_data.get('allergies')
            customer = Customer(first_name=first_name, last_name=last_name, email=email,
                                child_first_name=child_first_name, child_last_name=child_last_name, allergies=allergies)
            customer.save()
            return redirect(f'thankyou/{customer.id}/')
    else:
        form = RecipeForm()
    return render(request, 'recipes/home.html', {'form': form})


def recipe_list(request):
    return render(request, 'recipes/thankyou.html')
