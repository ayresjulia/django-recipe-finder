from django.db import models

# Customer model: recipes are not included in the initial RecipeForm, but added to db after form submission


class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=250)
    child_first_name = models.CharField(max_length=50)
    child_last_name = models.CharField(max_length=50)
    allergies = models.CharField(max_length=300)
    recipes = models.CharField(max_length=300)

    def __str__(self):
        return self.email
