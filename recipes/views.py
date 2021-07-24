from django.shortcuts import render,  redirect, get_object_or_404
from django.http import HttpResponse
from .models import Customer
from .forms import RecipeForm
import requests
import re

RECIPE_BASE_URL = "https://60f5adf918254c00176dffc8.mockapi.io/api/v1/recipes/"

# function for home page which shows RecipeForm, saves info to db and redirects to thank you page


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

# function for thankyou page which filters recipes according to customer allergies and saved recipes to db


def recipe_list(request, id):
    customer = get_object_or_404(Customer, pk=id)
    # regex to get rid of spec char in allergy str
    cust_allrg = re.sub('[^a-zA-Z,]+', '', customer.allergies)
    responses = requests.get(RECIPE_BASE_URL)
    if responses.status_code == 200:
        recipes = responses.json()
        filtered_recipes = [
            recipe for recipe in recipes if (recipe['allergens'] == [] or recipe['allergens'][0] not in customer.allergies)]
    db_recipe_list = []
    for item in filtered_recipes:
        db_recipe_list.append(item['name'])
    customer.recipes = db_recipe_list
    customer.save()
    return render(request, 'recipes/thankyou.html', {'cust_allrg': cust_allrg, 'customer': customer, 'filtered_recipes': filtered_recipes})
