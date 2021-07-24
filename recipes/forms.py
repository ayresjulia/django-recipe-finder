from django import forms
from .allergens import get_allergens

# getting BIG-8 common allergy choices
choices = get_allergens()

# RecipeForm uses available allergens in checkbox field


class RecipeForm(forms.Form):
    first_name = forms.CharField(label='first name', max_length=50)
    last_name = forms.CharField(label='last name', max_length=50)
    email = forms.EmailField(label='email', max_length=250)
    child_first_name = forms.CharField(
        label="child's first name", max_length=50)
    child_last_name = forms.CharField(label="child's last name", max_length=50)
    allergies = forms.MultipleChoiceField(
        label='choose allergies (if applicable)', required=False, choices=choices, widget=forms.CheckboxSelectMultiple)
